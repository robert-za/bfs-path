import random
from collections import deque


GRID_SIZE = 10


class LocationCoordinates:
    def __init__(self, name: str, max_x: int = GRID_SIZE, max_y: int = GRID_SIZE) -> None:
        self.name = name
        self.max_x = max_x
        self.max_y = max_y
        self.coordinates = (int(random.random() * self.max_x), int(random.random() * self.max_y))

    def __str__(self) -> str:
        return f"Generated Coordinates for {self.name}: {self.coordinates}"


class BreadthFirstSearch:
    POSSIBLE_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @classmethod
    def find_shortest_path(cls, start: LocationCoordinates, finish: LocationCoordinates):
        queue = deque([start.coordinates])
        parent = {tuple(start.coordinates): None}

        while queue:
            current_location = queue.popleft()

            if current_location == finish.coordinates:
                return cls._reconstruct_path(current_location, parent)

            for dx, dy in cls.POSSIBLE_DIRECTIONS:
                neighbor = (current_location[0] + dx, current_location[1] + dy)

                if 0 <= neighbor[0] < start.max_x + 1 and 0 <= neighbor[1] < finish.max_y + 1 and tuple(neighbor) not in parent:
                    queue.append(neighbor)
                    parent[tuple(neighbor)] = current_location

        return None

    @staticmethod
    def _reconstruct_path(
            current_location: tuple[int, int],
            parent: dict[tuple[int, int], tuple[int, int] | None]
    ) -> list[tuple[int, int] | None]:
        path = []
        while current_location:
            path.append(current_location)
            current_location = parent[current_location]
        return path[::-1]

for i in range(1):
    first_location = LocationCoordinates("A")
    second_location = LocationCoordinates("B")
    print(first_location)
    print(second_location)

    shortest_path = BreadthFirstSearch.find_shortest_path(first_location, second_location)
    if shortest_path:
        print("Shortest Path:", shortest_path)
    else:
        print("No path found.")  # it should not happen in closed system
