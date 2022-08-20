import requests


def get_api_url() -> str:
    return "http://localhost:8080/"


def test_api_returns_empty_list_when_no_plates() -> None:
    url = f"{get_api_url()}/plate"
    request = requests.get(url)

    assert request.status_code == 200
    assert request.json() == []


def test_api_allows_to_store_plate() -> None:
    url = f"{get_api_url()}/plate"
    data = {"plate": "M-PP123"}

    request = requests.post(url, json=data)

    assert request.status_code == 200
