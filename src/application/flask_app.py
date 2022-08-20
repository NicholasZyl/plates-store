import typing
from flask import Flask


app = Flask(__name__)


@app.route('/plate', methods=['GET'])
def get_plates() -> typing.List[typing.Dict[str, str]]:
    return []


@app.route('/plate', methods=['POST'])
def store_plate() -> str:
    pass


if __name__ == '__main__':
    app.run()
