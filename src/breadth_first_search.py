from collections import deque
from typing import Dict

from src.location import Location
from src.path import PathObject
from src.settings import POSSIBLE_DIRECTIONS


class BreadthFirstSearch:
    @classmethod
    def find_shortest_path(cls, start: Location, finish: Location) -> PathObject | None:
        queue = deque([start])
        parent = {start: None}

        while queue:
            current_location = queue.popleft()

            if current_location.coordinates == finish.coordinates:
                return cls._construct_path(current_location, parent)

            for dx, dy in POSSIBLE_DIRECTIONS:
                neighbor = Location()
                # TODO 2025-02-04: Implement x, y for coordinates obj to call by names and not indexes
                neighbor.coordinates = (current_location.coordinates[0] + dx, current_location.coordinates[1] + dy)

                if cls._is_neighbor_within_grid(neighbor) and cls._is_neighbour_visited(neighbor, parent):
                    queue.append(neighbor)
                    parent[neighbor] = current_location

        return None

    @staticmethod
    def _construct_path(current_location: Location | None, parent: Dict[Location, Location]) -> PathObject | None:
        path = PathObject()
        while current_location:
            path.append_location(current_location)
            current_location = parent[current_location]
        path.inverse_path()
        return path

    @staticmethod
    def _is_neighbor_within_grid(node: Location) -> bool:
        return 0 <= node.coordinates[0] < node.max_x + 1 and 0 <= node.coordinates[1] < node.max_y + 1

    @staticmethod
    def _is_neighbour_visited(node: Location, parent: Dict[Location, Location | None]) -> bool:
        return node.coordinates not in [location.coordinates for location in parent]
