from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['Get'])
def get():
    return jsonify({'msg': 'Python API running.'})


if __name__ == '__main__':
    app.run(port=7819)
