from http import HTTPStatus
from some_file import make_a_request


def test_make_a_request() -> None:
    assert make_a_request() == HTTPStatus.OK
