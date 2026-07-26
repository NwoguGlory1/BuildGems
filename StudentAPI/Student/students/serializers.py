#convert model instances into JSON and validate incoming JSON data

from rest_framework import serializers
from .models import Student, Department, Course

class StudentSerializerV1(serializers.ModelSerializer):
    "handles serialization & deserialization of student data automatically when using ModelViewSet"
#understand why this highlighted part
    department = serializers.SlugRelatedField( #Slug helps : Instead of looking up objects by their ID, look them up by another field
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


class StudentSerializerV2(serializers.ModelSerializer):
    "handles serialization & deserialization automatically when using ModelViewSet"
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'department' ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code']