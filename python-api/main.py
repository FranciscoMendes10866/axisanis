from bottle import get, run

@get('/')
def index():
    return { "msg": "Python API running." }

run(host='0.0.0.0', port=7819)
