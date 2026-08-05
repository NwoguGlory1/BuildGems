import requests

from django.conf import settings


class CountryService:

    @staticmethod
    def get_country(country_name):

        url = (
            f"{settings.COUNTRIES_API_BASE_URL}"
            f"/names.common/{country_name}"
        )
        # url = f"{settings.COUNTRIES_API_BASE_URL}/names.common/{country_name}"
        # follows this pattern https://api.restcountries.com/countries/v5/names.common/Canada
        # because the API doc says to call an endpoint like this


        headers = {
            "Authorization": f"Bearer {settings.COUNTRIES_API_KEY}"
        }

        response = requests.get(
            url=url,
            headers=headers,
            timeout=10, #prevents wait forever if the API hangs.
        )

        response.raise_for_status()
# If we made a bad request (a 4XX client error or 5XX server error response), we can raise it with Response.raise_for_status()

        data = response.json()
        #  turns the API response in json into a Python dictionary.

        country = data["data"]["objects"][0] #data["data"] gets the data object, data["data"]["objects"] gets the objects list,  [0] picks the first item in that list.

        return {

            "name": country["names"]["common"],

            "official_name": country["names"]["official"],

            "capital": country["capitals"][0]["name"],

            "region": country["region"],

            "subregion": country["subregion"],

            "flag": country["flag"]["emoji"],
        }
