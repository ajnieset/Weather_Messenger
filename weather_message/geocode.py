import toml

with open("configs/config.toml", "r") as cfg:
    CONFIG = toml.load(cfg)


def get_coordinates(location):
    pass
