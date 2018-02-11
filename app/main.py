
import json


def app(environ, start_response):
    start_response('200 OK', [
      ('Content-Type', 'text/plain'),
    ])
    yield json.dumps(handle()).encode('utf-8')


def handle():
    data = {
        'hello': 'world'
    }
    return data
