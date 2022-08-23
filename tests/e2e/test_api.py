import pytest
import requests

from freezegun import freeze_time


def get_api_url() -> str:
    return "http://localhost:8080/"


@pytest.mark.skip(reason="Work in progress on  e2e tests infra")
@pytest.mark.usefixtures("_with_clean_postgres_db")
def test_api_returns_empty_list_when_no_plates() -> None:
    url = f"{get_api_url()}/plate"
    request = requests.get(url)

    assert request.status_code == 200
    assert request.json() == []


@pytest.mark.skip(reason="Work in progress on  e2e tests infra")
def test_api_allows_to_store_plate() -> None:
    url = f"{get_api_url()}/plate"
    data = {"plate": "M-PP123"}

    request = requests.post(url, json=data)

    assert request.status_code == 200


@pytest.mark.skip(reason="Work in progress on  e2e tests infra")
@pytest.mark.usefixtures("_with_clean_postgres_db")
@freeze_time("2020-09-18T13:21:21Z")
def test_api_returns_stored_plate() -> None:
    url = f"{get_api_url()}/plate"

    license_plate = "M-PP123"
    data = {"plate": license_plate}
    requests.post(url, json=data)

    request = requests.get(url)
    response = request.json()

    assert request.status_code == 200
    assert type(response) is list
    assert len(response) == 1
    assert response[0]['plate'] == license_plate
    assert response[0]['timestamp'] == "2020-09-18T13:21:21Z"
