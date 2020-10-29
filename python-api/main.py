from bottle import get, run

@get('/')
def index():
    return 'Hello World'

run(host='localhost', port=7819)
