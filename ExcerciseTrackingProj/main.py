import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import datetime


load_dotenv()

today = datetime.datetime.now()

NUTRI_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRI_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRI_USER_ID = os.getenv("NUTRITIONIX_USER_ID")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_TOKEN = os.getenv("SHEETY_BASIC_TOKEN")
SHEETY_USERID = os.getenv("SHEETY_USER_NAME")
SHEETY_PASS = os.getenv("SHEETY_PASS_BASIC")
GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/b528a55444e1450cb1d458a3f37f7b89/newWorkout/workouts"
basic = HTTPBasicAuth(SHEETY_USERID, SHEETY_PASS)

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "x-remote-user-id": NUTRI_USER_ID,
}

sheet_header = {
    "Authorization": f"Basic {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}


body = {"query": input("What exercise you did?: "), 'gender': "male", 'weight_kg': 90.5, 'height_cm': 166.1, 'age': 28}

response = requests.post(url=NUTRI_ENDPOINT, json=body, headers=headers)
all_exercises = response.json()['exercises']

for exercise in all_exercises:
    sheet_body = {
        "workout": {
            "date": today.strftime("%x"),
            "time": today.strftime("%X"),
            "exercise": str(exercise["name"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    res = requests.post(url=GOOGLE_SHEET_ENDPOINT, json=sheet_body, auth=basic, headers=sheet_header)
    res.raise_for_status()
    print(res.json())


