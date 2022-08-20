import typing
from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/plate', methods=['GET'])
def get_plates() -> typing.List[typing.Dict[str, str]]:
    return []


@app.route('/plate', methods=['POST'])
def store_plate() -> str:
    data = request.get_json()
    if type(data) is not dict or "plate" not in data:
        raise BadRequest()

    return ''
