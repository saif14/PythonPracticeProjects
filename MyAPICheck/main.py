import os
from dotenv import load_dotenv
import requests
import binascii
import struct
import base64
import PIL.Image as Image
import io

load_dotenv()

end_point = os.getenv("END_POINT")

authorization = "Bearer "+ os.getenv("API_KEY")

param = {
    "accountNo": os.getenv("ACC_NO")
}

header = {
    "Authorization": authorization
}

response = requests.get(url=end_point, params=param, headers=header)
response.raise_for_status()
data = response.json()

# print(data['image'])
da = data['image']
binstr = base64.b64decode(da)
b = base64.b64decode(binstr)
ba = bytearray(binstr)
print(b)

img = Image.open(io.BytesIO(b))
img.show()
