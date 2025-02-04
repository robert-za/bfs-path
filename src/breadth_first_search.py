
from collections import deque

from src.location_coordinates import LocationCoordinates
from src.path import Path
from src.settings import POSSIBLE_DIRECTIONS


class BreadthFirstSearch:
    @classmethod
    def find_shortest_path(
            cls,
            start: LocationCoordinates,
            finish: LocationCoordinates
    ) -> list[tuple[int, int]] | None:
        queue = deque([start.coordinates])
        parent = {tuple(start.coordinates): None}

        while queue:
            current_location = queue.popleft()

            if current_location == finish.coordinates:
                return cls._reconstruct_path(current_location, parent).inverse_path()

            for dx, dy in POSSIBLE_DIRECTIONS:
                neighbor = (current_location[0] + dx, current_location[1] + dy)

                if 0 <= neighbor[0] < start.max_x + 1 and 0 <= neighbor[1] < finish.max_y + 1 and tuple(neighbor) not in parent:
                    queue.append(neighbor)
                    parent[tuple(neighbor)] = current_location

        return None

    @staticmethod
    def _reconstruct_path(
            current_location: tuple[int, int],
            parent: dict[tuple[int, int], tuple[int, int] | None]
    ) -> Path | None:
        path = Path()
        while current_location:
            path.append_step(current_location)
            current_location = parent[current_location]
        return path
