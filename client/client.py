import requests
import json
from .encryption import AESCipher
from .config import SERVER_URL

cipher = AESCipher()
data_to_send = 'this secret message'
encrypted_data = cipher.encrypt(data_to_send)

response = requests.post(SERVER_URL, json={'data': encrypted_data})
if response.status_code == 200:
    print(response.json())
else:
    print('Failed to send data')
