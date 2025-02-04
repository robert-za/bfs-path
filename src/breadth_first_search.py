
from collections import deque

from src.location_coordinates import LocationCoordinates


class BreadthFirstSearch:
    POSSIBLE_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @classmethod
    def find_shortest_path(
            cls,
            start: LocationCoordinates,
            finish: LocationCoordinates
    ) -> list[tuple[int, int] | None] | None:
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
