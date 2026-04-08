import requests
import os

from dotenv import load_dotenv

api_key = os.getenv("f4f167d2e82c0f1c54a1aba2f33f1efe")

url = "https://api.openweathermap.org/data/2.5/weather?q=Nairobi&APPID=f4f167d2e82c0f1c54a1aba2f33f1efe"

response = requests.get(url)

data =response.json()

temp = data["main"] ["temp"]
humidity = data ["main"] ["humidity"]
description = data["weather"][0]["description"]

if "clear" in description.lower():
   emoji ="☀️"
   
elif "cloud" in description.lower():
    emoji ="⛅"
    
elif "rainy" in description.lower():
    emoji="🌧️"
    
else:
    emoji="✨"
    
# print(temp)
# print(humidity)
# print(description)

print(f"weather in Nairobi:{description}{emoji}")
print(f"Temperature:{temp}°C")
print(f"Humidity:{humidity}%")