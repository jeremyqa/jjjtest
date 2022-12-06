import requests


def make_a_request() -> int:
    response = requests.get('https://example.com')
    return response.status_code
