"""
Redis fixed-window rate limiter.

Why this file exists:
- Login/signup endpoints are the #1 target for brute-force and bot abuse.
- DRF's built-in throttles are great for general "X requests/min per user",
  but for auth endpoints you usually want something explicit, keyed by
  IP + identifier, that you fully control (and can unit test easily).

Pattern implemented (this is the industry-standard "fixed window counter"):
  1. Build a Redis key from an identifier (IP, email, user id, etc.)
  2. INCR the key (atomic - safe under concurrent requests)
  3. If this is the first hit (count == 1), set a TTL on the key.
     Redis will auto-delete the key once the window expires - that's
     what "resets" the counter, no cron job needed.
  4. If count > limit -> reject with 429 before touching the view logic.

Docs:
- Redis INCR: https://redis.io/commands/incr/
- Redis EXPIRE / TTL: https://redis.io/commands/expire/
- Redis official rate limiting patterns: https://redis.io/tutorials/howtos/ratelimiting/
"""
import functools
import redis
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# One shared connection pool for the whole app.
# REDIS_URL should be set in settings.py / .env, e.g. redis://localhost:6379/0
redis_client = redis.from_url(
    getattr(settings, "REDIS_URL", "redis://localhost:6379/0"),
    decode_responses=True,
)


def get_client_ip(request):
    """
    Grab the real client IP, accounting for reverse proxies (Nginx, Render,
    Railway, etc.) that set X-Forwarded-For. Falls back to REMOTE_ADDR.
    """
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        # X-Forwarded-For can be a chain: "client, proxy1, proxy2"
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


class RateLimitExceeded(Exception):
    """Raised internally when a caller has exceeded their allowed rate."""
    pass


def check_rate_limit(key: str, limit: int, window_seconds: int) -> dict:
    """
    Core Redis logic. Returns a dict with count/remaining/allowed so callers
    (views, tests, other decorators) can inspect it.

    key            -> fully-formed redis key, e.g. "ratelimit:login:102.89.1.1"
    limit          -> max requests allowed inside the window
    window_seconds -> size of the fixed window, e.g. 300 for 5 minutes
    """
    # INCR creates the key at 1 if it doesn't exist yet - atomic, no race condition.
    current_count = redis_client.incr(key)

    if current_count == 1:
        # First request in this window -> start the TTL clock.
        redis_client.expire(key, window_seconds)

    allowed = current_count <= limit
    ttl = redis_client.ttl(key)

    return {
        "allowed": allowed,
        "count": current_count,
        "limit": limit,
        "remaining": max(0, limit - current_count),
        "retry_after": ttl if ttl and ttl > 0 else window_seconds,
    }


def rate_limit(limit: int, window_seconds: int, key_func=None, scope: str = "default"):
    """
    Decorator for DRF APIView.post/.get methods.

    Usage:
        @rate_limit(limit=5, window_seconds=300, scope="login")
        def post(self, request, *args, **kwargs):
            ...

    key_func: optional callable(request) -> str, to build the identifier.
              Defaults to client IP. For per-user limits, e.g. on an
              already-authenticated endpoint, pass:
                  key_func=lambda request: str(request.user.id)
    """
    def decorator(view_method):
        @functools.wraps(view_method)
        def wrapped(self, request, *args, **kwargs):
            identifier = key_func(request) if key_func else get_client_ip(request)
            redis_key = f"ratelimit:{scope}:{identifier}"

            result = check_rate_limit(redis_key, limit, window_seconds)

            if not result["allowed"]:
                return Response(
                    {
                        "detail": "Too many requests. Please try again later.",
                        "retry_after_seconds": result["retry_after"],
                    },
                    status=status.HTTP_429_TOO_MANY_REQUESTS,
                    headers={"Retry-After": str(result["retry_after"])},
                )

            response = view_method(self, request, *args, **kwargs)

            # Nice-to-have: expose rate limit info in headers, like real APIs do
            # (GitHub, Stripe, Twitter all do this).
            response["X-RateLimit-Limit"] = str(result["limit"])
            response["X-RateLimit-Remaining"] = str(result["remaining"])
            return response

        return wrapped

    return decorator