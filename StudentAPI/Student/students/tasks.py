# define all tasks in a separate tasks.py module
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def say_hello():
    send_mail(
       subject="Testing Celery",
        message="Celery is working!",
        from_email="darajanwogu@gmail.com",  # Use the same Gmail in EMAIL_HOST_USER in .env
        recipient_list=["glorynwogu19@gmail.com"],
        fail_silently=False,
    )