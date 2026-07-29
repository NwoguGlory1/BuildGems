from rest_framework.views import APIView
from rest_framework.response import Response
from students.services.countries import CountryService

class CountryAPIView(APIView):

    def get(self, request, country, **kwargs):

        data = CountryService.get_country(country)

        return Response(data)