from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from students.services.countries import CountryService


COUNTRIES_CACHE_TTL = 60 * 15


class CountryAPIView(APIView):

    def get(self, request, country, *args, **kwargs):

        # Create a cache key unique to this country
        cache_key = f"country:{country.lower()}"

        # Step 1: Check Redis
        cached_country = cache.get(cache_key)

        if cached_country is not None:
            return Response(
                {
                    "source": "cache",
                    "data": cached_country,
                }
            )

        # Step 2: Cache miss → call external API
        data = CountryService.get_country(country)

        # Step 3: Store in Redis
        cache.set(cache_key, data, COUNTRIES_CACHE_TTL)

        # Step 4: Return response
        return Response(
            {
                "source": "external api",
                "data": data,
            }
        )