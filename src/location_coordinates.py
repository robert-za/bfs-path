import random

from src.settings import GRID_SIZE


class LocationCoordinates:
    def __init__(self, name: str, max_x: int = GRID_SIZE, max_y: int = GRID_SIZE) -> None:
        self.name = name
        self.max_x = max_x
        self.max_y = max_y
        self.coordinates = (int(random.random() * self.max_x), int(random.random() * self.max_y))

    def __str__(self) -> str:
        return f"Generated Coordinates for {self.name}: {self.coordinates}"
