#  views for department-specific logic
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from students.models import Department
from students.serializers import DepartmentSerializer

DEPARTMENTS_CACHE_KEY = "departments:all"
DEPARTMENTS_CACHE_TTL = 60 * 15

class DepartmentListView(APIView):
    # GET "/api/v1/departments/"
    def get(self, request,  *args, **kwargs):
         # Step 1: Try cache first
        cached_data = cache.get(DEPARTMENTS_CACHE_KEY)

        if cached_data:
            return Response(
                {
                  "source": "cache",
                  "count": len(cached_data),
                  "data": cached_data  
                }
            )
         # Step 2: Cache MISS — query the database
        query_set = Department.objects.all()
        serializer_class = DepartmentSerializer(query_set, many=True)  #tells DRF how serialize/deserialize the Department data
        data = serializer_class.data

         # Step 3: Store in Redis with TTL
         # cache.set(key, value, timeout_in_seconds)
        cache.set(DEPARTMENTS_CACHE_KEY, data, DEPARTMENTS_CACHE_TTL)
        return Response(
           {
              "source": "database",
              "count": len(data),
              "data": data,
           }
        )