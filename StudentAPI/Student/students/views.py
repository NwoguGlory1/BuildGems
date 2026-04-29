# from django.shortcuts import render for normal rendering

# ViewSets provide CRUD operations in one place
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer



class StudentViewSet(viewsets.ModelViewSet): #ModelViewSet provides CRUD
    queryset = Student.objects.all() #defines the set of objects available via the API.
    serializer_class = StudentSerializer #tells DRF how serialize/deserialize the Student data
    # ModelViewSet automatically provides list, retrieve, create, update and destroy actions.

    @action(detail=True, methods=['GET'])
    # detail specifies whether the custom action is bound to a single instance of the resource (detail view) or to the entire resource collection (list view).
    
    def top_students(self, request, pk=None):
        # custom action logic for GET request
        students = Student.objects.filter(age__gte=100)
        # retrieves data/perform any operation based on the instance with 'pk'
        serializer = self.get_serializer(students, many=True)
        # when detail=True, the custom action is associated with a single instance of the resource and is accessed through the URL pattern containing the instance's primary key
        
        return Response({'message': f'Custom GET Action executed for instance {pk}'})
        # return Response({
        #     "status": "success",
        #     "data": serializer.data
        # })
    # to trigger GET : http://localhost:8000/myviewset/{pk}/custom_get_action/    


    @action(detail=False, methods=['POST'])
    def custom_post_action(self, request, pk=None):
    # custom action logic for POST request
    # perform any operation based with the posted data 
        return Response({'message': 'Custom POST Action executed successfully'})
    # to triggerPOST :http://localhost:8000/myviewset/custom_post_action/    
    #    when detail=False, the custom action is associated with the entire resource and is accessed through the URL pattern without any instance's primary key
