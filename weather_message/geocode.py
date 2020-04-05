import toml

from typing import Final

with open("configs/config.toml", "r") as cfg:
    CONFIG = toml.load(cfg)

GEOCODIO: Final = "https://api.geocod.io/v1.4/geocode"


def get_coordinates(location):
    pass
