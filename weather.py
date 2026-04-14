import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")



city =input("Enter city name:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data =response.json()

if data.get("cod") != 200:
    print("Error:", data.get("Error"))
else:
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
     print(f"weather in {city}:{description}{emoji}")
     print(f"Temperature:{temp}°C")
     print(f"Humidity:{humidity}%")