# define all tasks in a separate tasks.py module
from celery import shared_task

@shared_task
def say_hello():
    print("Hello from Celery!")