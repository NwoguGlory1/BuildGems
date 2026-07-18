# This ensures that the Celery app in celery.py is loaded and starts whenever Django starts.
# so that @shared_task in tasks.py will use it
from .celery import app as celery_app

__all__ = ("celery_app",)