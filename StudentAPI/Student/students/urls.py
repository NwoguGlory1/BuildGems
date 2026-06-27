# #create this file to define view routes
# from django.urls import path
# from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('students.auth.urls')),
    #matches /auth
]
# Using DefaultRouter, don’t need to manually define each URL for CRUD operations. It automatically creates standard RESTful endpoints 
