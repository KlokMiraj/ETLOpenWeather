import requests
import os

from weather_data_pipeline.app import api

api_key= os.getenv("API_KEY")
city = "London"

def get_weather_data():
    response = requests.get(f"http://api.openweathermap.org/data/3.0/weather?q={city}&appid={api_key}")
    print(response.json())
    return response.json()