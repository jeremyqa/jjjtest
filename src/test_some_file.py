from http import HTTPStatus
from unittest.mock import patch

from some_file import make_a_request, roll_fate


def test_make_a_request() -> None:
    assert make_a_request() == HTTPStatus.OK


def test_roll_fate_no_mock() -> None:
    assert -4 <= roll_fate(0) <= 4


class TestRollFate:
    def test_all_1s_returns_negative_four(self) -> None:
        with patch('some_file.randint', return_value=1):
            assert roll_fate(0) == -4
            assert roll_fate(0) == -4
            assert roll_fate(0) == -14
