import requests
import os

from dotenv import load_dotenv

api_key = os.getenv("f4f167d2e82c0f1c54a1aba2f33f1efe")

url = "https://api.openweathermap.org/data/2.5/weather?q=Nairobi&APPID=f4f167d2e82c0f1c54a1aba2f33f1efe"

response = requests.get(url)

print(response.json())