import requests
from dotenv import load_dotenv
import os

load_dotenv()

TEQUILLA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILLA_API_KEY = os.getenv("TEQUILAA_FLIGHT_SEARCH_API_KEY")

class FlightSearch:
    def __init__(self):
        self.iata_code = ""

    def get_iata_code(self, city: str):
        """Fetch IATA Code for a given city name"""

        location_end_point = f"{TEQUILLA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILLA_API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_end_point, headers=headers, params=query)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code