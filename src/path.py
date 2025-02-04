from typing import List, Tuple

from location import Location


class PathObject:
    def __init__(self) -> None:
        self.steps = []

    def append_location(self, location: Location) -> None:
        self.steps.append(location)

    def inverse_path(self) -> None:
        self.steps =  self.steps[::-1]
