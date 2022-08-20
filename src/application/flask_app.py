import os
import typing
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.exceptions import BadRequest, UnprocessableEntity

from src.application.container import container
from src.domain.repositories import LicensePlatesRepository
from src.domain.services import NonProcessablePlateNumber
from src.infrastructure.orm import SqlAlchemyLicensePlatesRepository, start_mappers


def get_db_uri() -> str:  # pragma: no cover
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    password = os.environ.get("DB_PASSWORD")
    if not host or not port or not password:
        raise Exception("Can't connect to the database.")

    user, db_name = "api", "plates_store"

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def create_app(test_repository: typing.Optional[LicensePlatesRepository] = None) -> Flask:
    app = Flask(__name__)
    if test_repository:
        app.testing = True
        repository = test_repository
    else:  # pragma: no cover
        start_mappers()
        repository = SqlAlchemyLicensePlatesRepository(
            sessionmaker(bind=create_engine(get_db_uri()))()
        )

    container.set_repository(repository)
    app.add_url_rule('/plate', view_func=get_plates, methods=['GET'])
    app.add_url_rule('/plate', view_func=store_plate, methods=['POST'])

    return app


def get_plates() -> typing.List[typing.Dict[str, str]]:
    return []


def store_plate() -> str:
    data = request.get_json()
    if type(data) is not dict or "plate" not in data:
        raise BadRequest()

    try:
        container.get_plates_store().store(data["plate"])
    except NonProcessablePlateNumber:
        raise UnprocessableEntity()

    return ''
