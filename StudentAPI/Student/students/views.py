# from django.shortcuts import render for normal rendering

# ViewSets provide CRUD operations in one place
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
import django_filters.rest_framework
from .models import Student
from .serializers import (StudentSerializerV1, StudentSerializerV2)
from .pagination import StudentPagination

class StudentViewSet(viewsets.ModelViewSet): #ModelViewSet provides CRUD
    queryset = Student.objects.all() #defines the set of objects available via the API.
    serializer_class = StudentSerializerV1 #tells DRF how serialize/deserialize the Student data
    # Custom pagination class
    pagination_class = StudentPagination
    # ModelViewSet automatically provides list, retrieve, create, update and destroy actions.
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # Automatic filtering using the special DRF config attribute, filterset_fields to filter:
    # filterset_fields = ['id', 'name', 'age']
    # example: {{student_base_url}}/students/?id=3&name=KesingKaesing BuildGems
    # {{student_base_url}}/students/?id=3&name=KesingKaesing BuildGems&age=87

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializerV1

#Helps avoid parse error on POSTMAN on delete request 
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({})
    
    # Manual filtering using .get_queryset()
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name') 
        id = self.request.query_params.get('id') 
        age = self.request.query_params.get('age') 
        if name:
            queryset = queryset.filter(name__icontains=name)
        if id:
           queryset = queryset.filter(id=id)
        if age:   
            queryset = queryset.filter(age__gte=age)
        return queryset

    @action(detail=False, methods=['GET'])
    # Use detail=True when working with ONE object, depends on pk which is for path params  
    def top_students(self, request):
        # custom action logic for GET request
        students = Student.objects.filter(age__gte=100)
        serializer = self.get_serializer(students, many=True)
        data = serializer.data  #After creating a serializer, you get serializer.data
        # print(type(data)) test this

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
