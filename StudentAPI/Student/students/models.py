from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    name  = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    birthday = models.DateField(null=True, blank=True)
    #relationship between student and courses
    courses = models.ManyToManyField(Course, blank=True,)

    def __str__(self):
        #returns human readable 
        # representation of each student instance
        return self.name
    