from django.db import models

# Create your models here.
class Student(models.Model):
    name  = models.CharField(max_length=200)
    age = models.DateField(max_length=20)
    email = models.EmailField(unique=True)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        #returns human readable representation of each student instance
        return self.name
