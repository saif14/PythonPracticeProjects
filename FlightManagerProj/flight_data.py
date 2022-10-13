import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILLA_API_KEY = os.getenv("TEQUILAA_FLIGHT_SEARCH_API_KEY")

class FlightData:
    def __init__(self):
        self.price = 0.0
        self.departure_airport_code = "LON"
        self.currency = "GBP"

    def get_price(self, destination_code):
        location_end_point = f"{TEQUILLA_ENDPOINT}/search"
        headers = {"apikey": TEQUILLA_API_KEY}
        today_time = datetime.datetime.now()
        today = today_time.strftime("%d/%m/%Y")
        date_to = today_time + datetime.timedelta(6*30)
        return_from = today_time + datetime.timedelta(7)
        return_to = today_time + datetime.timedelta(28)
        query_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": destination_code,
            "date_from": today,
            "date_to": date_to.strftime("%d/%m/%Y"),
            "return_from": return_from.strftime("%d/%m/%Y"),
            "return_to": return_to.strftime("%d/%m/%Y"),
            "curr": self.currency
        }
        # print(query_params)
        response = requests.get(url=location_end_point, headers=headers, params=query_params)
        response.raise_for_status()
        # print(response.json()["data"][0]["price"])
        return response.json()["data"][0]["price"], query_params

