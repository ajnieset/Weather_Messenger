from typing import Final

import requests
import toml


with open("configs/config.toml", "r") as cfg:
    CONFIG = toml.load(cfg)

DARKSKY: Final = "https://api.darksky.net/forecast/"


def get_daily_weather(latitude: str, longitude: str) -> dict:
    """ Returns the daily weather information for a week """

    return requests.get(
        DARKSKY + CONFIG["dark-sky"]["appid"] + f"/{latitude}, {longitude}"
    ).json()
