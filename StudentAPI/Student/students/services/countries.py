import requests

from django.conf import settings


class CountryService:

    @staticmethod
    def get_country(country_name):

        url = (
            f"{settings.COUNTRIES_API_BASE_URL}"
            f"/names.common/{country_name}"
        )

        headers = {
            "Authorization": f"Bearer {settings.COUNTRIES_API_KEY}"
        }

        response = requests.get(
            url=url,
            headers=headers,
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        country = data["data"]["objects"][0]
        return {

            "name": country["names"]["common"],

            "official_name": country["names"]["official"],

            "capital": country["capitals"][0]["name"],

            "region": country["region"],

            "subregion": country["subregion"],

            "flag": country["flag"]["emoji"],
        }
