from flask import Flask


app = Flask(__name__)


@app.route('/plate', methods=['GET'])
def get_plates():
    return []


@app.route('/plate', methods=['POST'])
def store_plate():
    return ''


if __name__ == '__main__':
    app.run()
