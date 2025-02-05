import random
import secrets
from typing import Tuple

from src.settings import GRID_SIZE


class Location:
    def __init__(self, name: str | None = None, max_x: int = GRID_SIZE, max_y: int = GRID_SIZE) -> None:
        self._name: str = name if name else self._generate_hex_name()
        self._max_x: int = max_x
        self._max_y: int = max_y
        self._coordinates: Tuple[int, int] | None = None

    def __str__(self) -> str:
        return f"{self._name}: {self._coordinates}"

    def __hash__(self):
        return hash(self.coordinates)

    def __eq__(self, other):
        return isinstance(other, Location) and self.coordinates == other.coordinates

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates: Tuple[int, int]) -> None:
        if not isinstance(new_coordinates, Tuple):
            raise TypeError("Coordinates must be a tuple of integers")
        self._coordinates = new_coordinates

    @property
    def max_x(self) -> int:
        return self._max_x

    @property
    def max_y(self) -> int:
        return self._max_y

    @staticmethod
    def _generate_hex_name() -> str:
        return secrets.token_hex(3)


class RandomLocation(Location):
    def __init__(self, name: str | None = None, max_x: int = GRID_SIZE, max_y: int = GRID_SIZE) -> None:
        super().__init__(name, max_x, max_y)
        self._coordinates: Tuple[int, int] = (int(random.random() * self._max_x), int(random.random() * self._max_y))
