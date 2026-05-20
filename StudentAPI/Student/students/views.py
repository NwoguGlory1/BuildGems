# from django.shortcuts import render for normal rendering

# ViewSets provide CRUD operations in one place
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters.rest_framework

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet): #ModelViewSet provides CRUD
    queryset = Student.objects.all() #defines the set of objects available via the API.
    serializer_class = StudentSerializer #tells DRF how serialize/deserialize the Student data
    # ModelViewSet automatically provides list, retrieve, create, update and destroy actions.
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # using the special DRF config attribute, filterset_fields to filter:
    filterset_fields = ['id', 'name', 'age']
# example: {{student_base_url}}/students/?id=3&name=KesingKaesing BuildGems
# {{student_base_url}}/students/?id=3&name=KesingKaesing BuildGems&age=87


    @action(detail=False, methods=['GET'])
    # Use detail=True when working with ONE object, depends on pk   
    def top_students(self, request):
        # custom action logic for GET request
        students = Student.objects.filter(age__gte=100)
  
        serializer = self.get_serializer(students, many=True)
       
        data = serializer.data  #After creating a serializer, you get serializer.data
        # print(type(data))

        # DRF received the response object & calls renderer automatically
        # CustomRenderer is global from settings.py, so you dont need to call it
        return Response(serializer.data)



    # @action(detail=False, methods=['POST'])
    # def custom_post_action(self, request, pk=None):
    # # custom action logic for POST request
    # # perform any operation based with the posted data 
    #     return Response({'message': 'Custom POST Action executed successfully'})
    # # to triggerPOST :http://localhost:8000/myviewset/custom_post_action/    
    #    when detail=False, the custom action is associated with the entire resource
    #  and is accessed through the URL pattern without any instance's primary key, /students/top_students
