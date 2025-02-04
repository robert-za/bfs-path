import secrets
from unittest.mock import patch

import pytest

from location import Location
from path import PathObject


@pytest.fixture(autouse=True)
def mock_token_hex():
    with patch.object(secrets, "token_hex", return_value="abcdef"):
        yield


class TestPathObject:
    def test_append_location(self) -> None:
        # given
        path = PathObject()
        location = Location()

        # when
        path.append_location(location)

        # then
        assert path.steps[0] == location

    def test_inverse_path(self) -> None:
        # given
        path = PathObject()
        location_a = Location()
        location_a.coordinates = (0, 0)
        location_b = Location()
        location_b.coordinates = (1, 1)
        path.append_location(location_a)
        path.append_location(location_b)

        # when
        assert path.steps[0] == location_a
        assert path.steps[-1] == location_b
        path.inverse_path()

        # then
        assert path.steps[0] == location_b
        assert path.steps[-1] == location_a
