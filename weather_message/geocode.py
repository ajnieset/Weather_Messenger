import toml
from geocodio import GeocodioClient  # type: ignore


with open("configs/config.toml", "r") as cfg:
    CONFIG = toml.load(cfg)


def get_coordinates(location: str) -> tuple:
    client = GeocodioClient(CONFIG["geocod"]["key"])
    return client.geocode(location).coords
