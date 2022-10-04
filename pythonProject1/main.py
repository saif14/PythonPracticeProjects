import json

import requests
from datetime import datetime

MY_LAT = 23.810331
MY_LONG = 90.412521


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


def get_hour(time):
    """Converting UTC to Dhaka, Bangladesh time"""
    data = {
        "fromTimeZone": "Etc/UTC",
        "dateTime": time,
        "toTimeZone": "Asia/Dhaka",
        "dstAmbiguity": ""
    }
    time_convert_response = requests.post("https://timeapi.io/api/Conversion/ConvertTimeZone", json=data)
    time_convert_response.raise_for_status()
    converted_time = time_convert_response.json()["conversionResult"]["dateTime"]
    print(converted_time)
    converted_time = converted_time.split("T")[1].split(":")[0]
    return converted_time


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = sunrise.replace("T", " ")
sunrise = sunrise.split("+")[0]
sunrise = get_hour(sunrise)

sunset = sunset.replace("T", " ")
sunset = sunset.split("+")[0]
sunset = get_hour(sunset)

time_now = datetime.now()
print(sunrise)
print(sunset)
