import requests
from datetime import datetime

MY_LAT = 23.810331
MY_LONG = 90.412521


def get_hour(time):
    """Converting UTC to Dhaka, Bangladesh time"""
    json_data = {
        "fromTimeZone": "Etc/UTC",
        "dateTime": time,
        "toTimeZone": "Asia/Dhaka",
        "dstAmbiguity": ""
    }
    time_convert_response = requests.post("https://timeapi.io/api/Conversion/ConvertTimeZone", json=json_data)
    time_convert_response.raise_for_status()
    converted_time = time_convert_response.json()["conversionResult"]["dateTime"]
    print(converted_time)
    converted_time = converted_time.split("T")[1].split(":")[0]
    return int(converted_time)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"iss lat {iss_latitude}")
    print(f"iss long {iss_longitude}")

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 6 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 6 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise = sunrise.replace("T", " ")
    sunrise = sunrise.split("+")[0]
    sunrise = get_hour(sunrise)

    sunset = sunset.replace("T", " ")
    sunset = sunset.split("+")[0]
    sunset = get_hour(sunset)

    print(sunset)
    print(sunrise)
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if is_iss_overhead() and is_night():
    print("Maathar upore!")
    # function to write a mail to see the iss
else:
    print("nai upore nai!")
