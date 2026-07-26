#  views for course-specific logic
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from students.models import Course
from students.serializers import CourseSerializer

COURSES_DATA = [
    {"id": 1, "name": "Introduction to Computer Science", "code": "CS101", "credits": 3},
    {"id": 2, "name": "Data Structures & Algorithms",    "code": "CS201", "credits": 4},
    {"id": 3, "name": "Database Systems",                "code": "CS301", "credits": 3},
    {"id": 4, "name": "Web Development",                 "code": "CS401", "credits": 3},
    {"id": 5, "name": "Machine Learning",                "code": "CS501", "credits": 4},
    {"id": 6, "name": "Blockchain & Distributed Systems","code": "CS601", "credits": 3}
]

class CourseListView(APIView):
    # GET /api/v1/courses/

    def get(self, request, *args, **kwargs):
        # Django may pass URL keyword arguments such as version from the URL pattern.
        # Accepting *args and **kwargs keeps this view compatible with versioned routes.
        return Response({
            "count": len(COURSES_DATA),
            "data": COURSES_DATA,
        })
    
class CourseStudentView(APIView):
    # """GET /api/v1/courses/students/"""
    def get(self, request,  *args, **kwargs):
        query_set = Course.objects.all()
        # query_set = Course.objects.get(name="Mathematics")
        serializer_class = CourseSerializer(query_set, many=True)  #tells DRF how serialize/deserialize the Course data
        data = serializer_class.data

        return Response(
           {
              "data": data,
           }   
        )
    def post(self, request,  *args, **kwargs):
        # """" POST {{student_base_url}}/v1/courses/students/"""
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


