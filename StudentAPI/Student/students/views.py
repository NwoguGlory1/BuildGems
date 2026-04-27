# from django.shortcuts import render for normal rendering

# ViewSets provide CRUD operations in one place
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet): #ModelViewSet provides CRUD
    queryset = Student.objects.all() #defines the set of objects available via the API.
    serializer_class = StudentSerializer #tells DRF how serialize/deserialize the Student data

    # ModelViewSet automatically provides list, retrieve, create, update and destroy actions.
    