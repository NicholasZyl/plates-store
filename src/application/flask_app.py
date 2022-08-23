import typing
from flask import Flask, request
from sqlalchemy.engine import Engine
from werkzeug.exceptions import BadRequest, UnprocessableEntity, Conflict

from src.application.flask_commands import init_command
from src.application.container import container
from src.domain.repositories import LicenseAlreadyStored
from src.domain.services import NonProcessablePlateNumber


def create_app(test_db: typing.Optional[Engine] = None) -> Flask:
    app = Flask(__name__)
    if test_db:
        app.testing = True
        container.set_db(test_db)

    app.add_url_rule('/plate', view_func=get_plates, methods=['GET'])
    app.add_url_rule('/plate', view_func=store_plate, methods=['POST'])
    app.register_blueprint(init_command)

    return app


def get_plates() -> typing.List[typing.Dict[str, str]]:
    return [
        {"plate": plate.number, "timestamp": plate.timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')}
        for plate in container.get_plates_store().retrieve()
    ]


def store_plate() -> str:
    data = request.get_json()
    if type(data) is not dict or "plate" not in data:
        raise BadRequest()

    try:
        container.get_plates_store().store(data["plate"])
    except NonProcessablePlateNumber:
        raise UnprocessableEntity()
    except LicenseAlreadyStored:
        raise Conflict()

    return ''
