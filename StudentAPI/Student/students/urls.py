# #create this file to define view routes
# from django.urls import path
# from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .courses.views import CourseListView
from .departments.views import  DepartmentListView
from .courses.views import CourseStudentView
from .services.views import CountryAPIView

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('students.auth.urls')),
    #matches /auth
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/students/', CourseStudentView.as_view(), name='course-student'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('countries/<str:country>/', CountryAPIView.as_view(), name="country-detail"),
]
# Using DefaultRouter, don’t need to manually define each URL for CRUD operations. It automatically creates standard RESTful endpoints 