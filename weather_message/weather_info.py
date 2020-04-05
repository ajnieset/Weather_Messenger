import requests

URL = ""


def get_weather_week():
    return requests.get(URL).json()
