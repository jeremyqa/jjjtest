import requests
from random import randint


def make_a_request() -> int:
    response = requests.get('https://example.org')
    return response.status_code


def roll_fate(bonus: int = 0) -> int:
    return sum([_fate_to_number(randint(1, 6)) for _ in range(4)]) + bonus


def _fate_to_number(raw: int) -> int:
    if raw < 3:
        return -1
    if raw > 4:
        return 1
    return 0
