from typing import Generator

import pytest
from flask.testing import FlaskClient

from src.application.flask_app import app


@pytest.fixture()
def test_client() -> Generator[FlaskClient, None, None]:
    app.testing = True

    with app.test_client() as client:
        yield client


def test_get_plates_endpoint_returns_list(test_client: FlaskClient) -> None:
    response = test_client.get('/plate')

    assert response.status_code == 200
    assert response.json == []


def test_store_plates_endpoint_accepts_plate_numbers(test_client: FlaskClient) -> None:
    response = test_client.post('/plate', json={"plate": "M-PP123"})

    assert response.status_code == 200


def test_store_plates_endpoint_fails_with_empty_request(test_client: FlaskClient) -> None:
    response = test_client.post('/plate')

    assert response.status_code == 400


def test_store_plates_endpoint_fails_with_malformed_request(test_client: FlaskClient) -> None:
    response = test_client.post('/plate', json={"data": "M-PP123"})

    assert response.status_code == 400
