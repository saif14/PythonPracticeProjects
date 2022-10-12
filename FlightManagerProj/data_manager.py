import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


load_dotenv()


class DataManager:
    def __init__(self):
        self.SHEETY_TOKEN = os.getenv("SHEETY_BASIC_TOKEN")
        self.SHEETY_USERID = os.getenv("SHEETY_USER_NAME")
        self.SHEETY_PASS = os.getenv("SHEETY_PASS_BASIC")

        self.basic = HTTPBasicAuth(self.SHEETY_USERID, self.SHEETY_PASS)
        self.sheet_header = {
            "Authorization": f"Basic {self.SHEETY_TOKEN}",
            # "Content-Type": "application/json"
        }

    def get_row(self):
        GOOGLE_SHEET_ENDPOINT_GET = "https://api.sheety.co/b528a55444e1450cb1d458a3f37f7b89/flightDeals/prices"
        res = requests.get(url=GOOGLE_SHEET_ENDPOINT_GET, auth=self.basic, headers=self.sheet_header)
        res.raise_for_status()
        return res.json()['prices']

    def update_row_data(self, row_id, column_name, updated_value):
        """It will update row in the google sheet"""
        GOOGLE_SHEET_ENDPOINT_PUT=f"https://api.sheety.co/b528a55444e1450cb1d458a3f37f7b89/flightDeals/prices/{row_id}"
        update_body = {
            "price": {
                column_name: updated_value
            }
        }
        res = requests.put(url=GOOGLE_SHEET_ENDPOINT_PUT, json=update_body, auth=self.basic, headers=self.sheet_header)

