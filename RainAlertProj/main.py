import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "d628bcc349ceb4b0533b2177d4cca0a2"

MY_LAT = 12.449229
MY_LONG = 98.627060

weather_params={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

forecast_data = response.json()["list"]

# Fetching current weather data for next 15 hours, with 3 hours interval as per API
weather_data = [forecast_data[i]['weather'][0]['id'] for i in range(0, 6)]

print(weather_data)
will_rain = False

for condition_code in weather_data:
    if condition_code < 600:
        print("Bring Umbrella!")
        will_rain = True
        break

if will_rain:
    print("Bring Umbrella")

"""
code to send sms with Twillio.
But cannot do this because Twillio is shit! So, Leaving it here!
"""