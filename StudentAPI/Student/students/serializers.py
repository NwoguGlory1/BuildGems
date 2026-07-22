#convert model instances into JSON and validate incoming JSON data

from rest_framework import serializers
from .models import Student, Department, Course

class StudentSerializer(serializers.ModelSerializer):
    """Serialize student data and accept department/course names in incoming payloads."""
    department = serializers.SlugRelatedField(
        queryset=Department.objects.all(),
        slug_field='name',
        required=False,
        allow_null=True,
    )
    courses = serializers.SlugRelatedField(
        queryset=Course.objects.all(),
        slug_field='name',
        many=True,
        required=False,
    )
    birthday = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'department', 'birthday', 'courses']


class StudentSerializerV1(StudentSerializer):
    """Version 1 exposes the full student payload for the API."""
    pass


class StudentSerializerV2(StudentSerializer):
    """Version 2 keeps the same payload structure for compatibility."""
    pass


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']