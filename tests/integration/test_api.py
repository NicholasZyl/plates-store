from typing import Generator

import pytest
from flask.testing import FlaskClient
from freezegun import freeze_time
from sqlalchemy.engine import Engine

from src.application.flask_app import create_app
from src.infrastructure.orm import metadata


@pytest.fixture()
def test_client(in_memory_db_engine: Engine) -> Generator[FlaskClient, None, None]:
    app = create_app(in_memory_db_engine)

    with app.test_client() as client:
        yield client
    metadata.drop_all(in_memory_db_engine)
    metadata.create_all(in_memory_db_engine)


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


@freeze_time("2020-09-18T13:21:21Z")
def test_store_plates_endpoint_fails_with_conflict_if_same_plate_tries_to_be_stored(test_client: FlaskClient) -> None:
    test_client.post('/plate', json={"plate": "M-PP123"})
    response = test_client.post('/plate', json={"plate": "M-PP123"})

    assert response.status_code == 409


@freeze_time("2020-09-18T13:21:21Z")
def test_get_plates_endpoint_returns_stored_plates(test_client: FlaskClient) -> None:
    test_client.post('/plate', json={"plate": "M-PP123"})

    plates = test_client.get('/plate').json

    assert plates is not None
    assert len(plates) == 1
    assert plates[0]["plate"] == "M-PP123"
    assert plates[0]['timestamp'] == "2020-09-18T13:21:21Z"
