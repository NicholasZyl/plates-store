from flask import Flask


app = Flask(__name__)


@app.route('/plate')
def get_plates():
    return '[]'


if __name__ == '__main__':
    app.run()
