import typing
from flask import Flask


app = Flask(__name__)


@app.route('/plate', methods=['GET'])
def get_plates() -> typing.List[typing.Dict[str, str]]:
    return []


@app.route('/plate', methods=['POST'])
def store_plate() -> str:
    return ''
