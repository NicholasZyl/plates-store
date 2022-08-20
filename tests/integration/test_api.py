from typing import Generator

import pytest
from flask.testing import FlaskClient

from src.application.flask_app import create_app
from src.domain.repositories import LicensePlatesRepository


@pytest.fixture()
def test_client(in_memory_repository: LicensePlatesRepository) -> Generator[FlaskClient, None, None]:
    app = create_app(in_memory_repository)

    with app.test_client() as client:
        yield client


def test_get_plates_endpoint_returns_list(test_client: FlaskClient) -> None:
    response = test_client.get('/plate')

    assert response.status_code == 200
    assert response.json == []


def test_store_plates_endpoint_accepts_plate_numbers(test_client: FlaskClient) -> None:
    response = test_client.post('/plate', json={"plate": "M-PP123"})

    assert response.status_code == 200


def test_store_plates_endpoint_fails_with_bad_request_with_empty_request(test_client: FlaskClient) -> None:
    response = test_client.post('/plate')

    assert response.status_code == 400


def test_store_plates_endpoint_fails_with_bad_request_with_malformed_request(test_client: FlaskClient) -> None:
    response = test_client.post('/plate', json={"data": "M-PP123"})

    assert response.status_code == 400


def test_store_plates_endpoint_fails_with_unprocessable_if_input_is_not_german_plate(test_client: FlaskClient) -> None:
    response = test_client.post('/plate', json={"plate": "W12345"})

    assert response.status_code == 422
