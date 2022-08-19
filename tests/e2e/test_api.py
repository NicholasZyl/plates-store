import requests


def test_api_returns_empty_list_when_no_plates():
    url = "http://localhost:8080/plate"
    request = requests.get(url)

    assert request.status_code == 200
