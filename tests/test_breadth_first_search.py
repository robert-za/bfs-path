import pytest

from src.breadth_first_search import BreadthFirstSearch
from src.location_coordinates import LocationCoordinates


class TestBreadthFirstSearch:
    @pytest.fixture
    def location_a(self) -> LocationCoordinates:
        return LocationCoordinates("A")

    @pytest.fixture
    def location_b(self) -> LocationCoordinates:
        return LocationCoordinates("B")

    def test_max_distance(self, location_a, location_b) -> None:
        # given
        location_a.coordinates = 0, 0
        location_b.coordinates = 9, 9

        # when
        path = BreadthFirstSearch.find_shortest_path(location_a, location_b)

        # then
        assert path == [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
            (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)
        ]

    def test_overlying_locations(self, location_a, location_b) -> None:
        # given
        location_a.coordinates = 0, 0
        location_b.coordinates = 0, 0

        # when
        path = BreadthFirstSearch.find_shortest_path(location_a, location_b)

        # then
        assert path == [(0, 0)]
