#  views for course-specific logic
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

COURSES_DATA = [
    {"id": 1, "name": "Introduction to Computer Science", "code": "CS101", "credits": 3},
    {"id": 2, "name": "Data Structures & Algorithms",    "code": "CS201", "credits": 4},
    {"id": 3, "name": "Database Systems",                "code": "CS301", "credits": 3},
    {"id": 4, "name": "Web Development",                 "code": "CS401", "credits": 3},
    {"id": 5, "name": "Machine Learning",                "code": "CS501", "credits": 4},
    {"id": 6, "name": "Blockchain & Distributed Systems","code": "CS601", "credits": 3}
]

class CourseListView(APIView):
    # GET /api/v1/auth/courses/

    def get(self, request, *args, **kwargs):
        # Django may pass URL keyword arguments such as version from the URL pattern.
        # Accepting *args and **kwargs keeps this view compatible with versioned routes.
        return Response({
            "count": len(COURSES_DATA),
            "data": COURSES_DATA,
        })
    
# class CourseDetailView(APIView):
#     """GET /api/v1/courses/<int:course_id>/"""
#     def get(self, request, course_id):
#         course = next(
#             (c for c in COURSES_DATA if c["id"] == course_id),
#             None
#         )

#         if not course:
#             return Response(
#                 {"detail": f"Course with id {course_id} not found."},
#                 status=404,
#             )

#         return Response({"data": course})