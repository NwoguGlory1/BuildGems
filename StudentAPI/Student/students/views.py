# from django.shortcuts import render for normal rendering

# ViewSets provide CRUD operations in one place
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from .utils.response import api_response



class StudentViewSet(viewsets.ModelViewSet): #ModelViewSet provides CRUD
    queryset = Student.objects.all() #defines the set of objects available via the API.
    serializer_class = StudentSerializer #tells DRF how serialize/deserialize the Student data
    # ModelViewSet automatically provides list, retrieve, create, update and destroy actions.


    @action(detail=False, methods=['GET'])
    # Use detail=True when working with ONE object, depends on pk   
    def top_students(self, request):
        # custom action logic for GET request
        students = Student.objects.filter(age__gte=100)
  
        serializer = self.get_serializer(students, many=True)
       
        data = serializer.data 
        return api_response( success=True,
            message="Retrieved successfully",
            data=data,
            errors=None
            )


    # @action(detail=False, methods=['POST'])
    # def custom_post_action(self, request, pk=None):
    # # custom action logic for POST request
    # # perform any operation based with the posted data 
    #     return Response({'message': 'Custom POST Action executed successfully'})
    # # to triggerPOST :http://localhost:8000/myviewset/custom_post_action/    
    #    when detail=False, the custom action is associated with the entire resource
    #  and is accessed through the URL pattern without any instance's primary key, /students/top_students
