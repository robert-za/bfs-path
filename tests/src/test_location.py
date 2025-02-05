import secrets
from unittest.mock import patch, Mock

import pytest

from location import Location


@pytest.fixture(autouse=True)
def mock_token_hex():
    with patch.object(secrets, "token_hex", return_value="abcdef"):
        yield


class TestLocation:
    def test_generate_hex_name(self) -> None:
        assert Location._generate_hex_name() == "abcdef"

    def test_string_repr_when_coords_are_none(self) -> None:
        # given
        location = Location()

        # then
        assert str(location) == "abcdef: None"

    def test_string_repr_when_coords_are_not_none(self) -> None:
        # given
        location = Location()
        location.coordinates = (0, 0)

        # then
        assert str(location) == "abcdef: (0, 0)"
