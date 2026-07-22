# define all tasks in a separate tasks.py module
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Student
from datetime import date
from students.models import Course


@shared_task
def send_email_to_student(student_id):
# Fetch one student by ID,Personalize the subject and message Send one email.
# Task send_email_to_student(student_idcalls send_mail
# student.department.name
    student = Student.objects.get(pk=student_id)
    # for debuging:
    # print(settings.EMAIL_HOST)
    # print(settings.EMAIL_PORT)
    # print(settings.EMAIL_USE_TLS)
    # print(settings.EMAIL_HOST_USER)
    # print(student.name)
    # print(student.id)
    # print(student.email)

    message = f"""
            Hello, {student.name}
            """
      
    send_mail(
        subject="Testing Celery",
        message=message,
        from_email= settings.DEFAULT_FROM_EMAIL,  # Use the same Gmail in EMAIL_HOST_USER in .env
        recipient_list=[student.email],
        fail_silently=False,
        )
    print("Voila, Email Sent!")
    return

@shared_task
def send_email_to_all_students():
# Query Student.objects.all()
    students = Student.objects.all()

#  loop through students,Queue send_email_to_student.delay(student.id) for each
# this task should not call send_mail() again
    for student in students:
        send_email_to_student.delay(student.id)

        
@shared_task
def send_birthday_emails():
# Students with birthdays today, loop, queue task 1
    today = date.today()
    students = Student.objects.filter(
        birthday__month=today.month,
        birthday__day=today.day,
        )
    for student in students:
        send_email_to_student.delay(student.id)

@shared_task
def send_math_students_email():

    maths = Course.objects.get(name="Mathematics")
    students = maths.student_set.all()

    for student in students:
        send_email_to_student.delay(student.id)

#OR:
    # students = Student.objects.filter(
    #     courses__name="Mathematics"
    #     )
    # for student in students:
    #         send_email_to_student.delay(student.id)