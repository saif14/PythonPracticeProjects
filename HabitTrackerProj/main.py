import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

PIXELA_USER_KEY = os.getenv("PIXELA_USER_KEY")
PIXELA_USER_NAME = os.getenv("PIXELA_USER_NAME")
GRAPH_ID = "graph1"

yesterday = date.today() - timedelta(1)
today = date.today()
d1 = today.strftime("%Y%m%d")
yd = yesterday.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER_NAME}/graphs/"
pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}"
pixel_update_endpoint = f"{pixela_endpoint}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}/{yd}"

user_params = {
    "token": PIXELA_USER_KEY,
    "username": PIXELA_USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_USER_KEY
}

pixel_data = {
    "date": d1,
    "quantity": "6.5"
}

pixel_update_data = {
    "quantity": "6.5"
}

# print(PIXELA_USER_KEY)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


"""POST request"""
# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r.text)


# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.json())


"""UPDATE request"""
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.json())


"""DELETE request"""
response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.json())