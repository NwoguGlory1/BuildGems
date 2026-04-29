#convert model instances into JSON and validate incoming JSON data

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    "handles serialization & deserialization automatically when using ModelViewSet"
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email']
# fields tuple specifies which model fields to expose via the API.
# id field (primary key) is included to uniquely identify each record.
