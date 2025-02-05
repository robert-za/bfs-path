from location import Location


class Path:
    def __init__(self) -> None:
        self.steps = []

    def append_location(self, location: Location) -> None:
        self.steps.append(location)

    def inverse_path(self) -> None:
        self.steps =  self.steps[::-1]
