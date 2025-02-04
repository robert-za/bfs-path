import pytest

from src.path import PathObject
from src.breadth_first_search import BreadthFirstSearch
from src.location import Location, RandomLocation


class TestBreadthFirstSearch:
    @pytest.fixture
    def location_a(self) -> Location:
        return Location("A")

    @pytest.fixture
    def location_b(self) -> Location:
        return Location("B")

    def test_max_distance(self, location_a, location_b) -> None:
        # given
        location_a.coordinates = 0, 0
        location_b.coordinates = 9, 9

        # when
        path = BreadthFirstSearch.find_shortest_path(location_a, location_b)

        # then

        assert isinstance(path, PathObject)
        assert len(path.steps) == 19
        assert path.steps[0] == location_a
        assert path.steps[-1].coordinates == location_b.coordinates

    def test_overlying_locations(self, location_a, location_b) -> None:
        # given
        location_a.coordinates = 0, 0
        location_b.coordinates = 0, 0

        # when
        path = BreadthFirstSearch.find_shortest_path(location_a, location_b)

        # then
        assert len(path.steps) == 1
        assert path.steps[0] == location_a

    def test_random_cases(self) -> None:
        # TODO 2025-02-04: Remove this test later
        for i in range(100):
            # given
            location_a = RandomLocation("A")
            location_b = RandomLocation("B")

            # when
            path = BreadthFirstSearch.find_shortest_path(location_a, location_b)

            # then
            assert path.steps[0] == location_a
            assert path.steps[-1].coordinates == location_b.coordinates
