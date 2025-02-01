
import requests


def _get_weather_data():
    API_KEY = "e5fa9a3ca72f741ca0de4b1c4b04c09"
    # API_KEY = os.environ.get("WEATHER_API_KEY")
    # API_KEY = Variable.get("weather_api_key")

    payload = {
        "q": "bangkok",
        "appid": API_KEY,
        "units": "metric"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=payload)
    print(response.url)

    data = response.json()
    print(data)

