import requests
from datetime import datetime
from config import Config
from common.functions import kelvin_to_celsius, ms_to_kmh

def get_weather():
    api_key = Config.api_key
    city = Config.api_city
    # api_key = "7283cdc2c5f2205aa7a051b9afc83be6"
    # city = "Lisbon"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try :
        response = requests.get(url)
        data = response.json()

        weather = {
            "temp": kelvin_to_celsius(data.get("main").get("temp")),
            "feels_like": kelvin_to_celsius(data.get("main").get("feels_like")),
            "name": data.get("name"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pressure": data.get("main").get("pressure"),
            "humidity": data.get("main").get("humidity"),
            "description": data.get("weather")[0].get("description"),
            "wind_speed": ms_to_kmh(data.get("wind").get("speed")),

        }

        return weather
    except Exception as e :
        print(e)

