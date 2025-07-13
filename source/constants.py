import os

from source.game import Game


FONT = ("Arial", 10, "bold")
ARMOUR_WIDTH = 0.70
TOTALS_WIDTH = 0.245
PADX = 25

DATA_FOLDER = "data"

for game in Game:
    os.makedirs(f"{DATA_FOLDER}_{game}", exist_ok=True)

STAR = "☆"

STORING_SEPARATOR = "::"
