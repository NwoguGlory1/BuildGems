# elery.py module that defines the Celery instance:
# this instance is used as the entry-point for everything you want to do in Celery, like creating tasks and managing workers, it must be possible for other modules to import it.
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Student.settings"
)

#app instance
app = Celery("Student")
# The first argument to Celery is the name of the current module. 

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration options
#   should be specified in uppercase, `CELERY_` prefix.
# example the task_always_eager setting becomes CELERY_TASK_ALWAYS_EAGER, and the broker_url setting becomes CELERY_BROKER_URL
#This also applies to the workers settings, for instance, the worker_concurrency setting becomes CELERY_WORKER_CONCURRENCY.
app.config_from_object(
    "django.conf:settings",
    namespace="CELERY"
)
# Load task modules from all registered Django apps.
app.autodiscover_tasks()