import json
from flask import Flask, jsonify, request

from .services.PersonService import retrieve, create

app = Flask(__name__)


@app.route('/rest')
def health():
    return jsonify({'response': 'Hello People this is Christian !'})


@app.route('/person_api/persons', methods=['GET', 'POST'])
def locations():
    if request.method == 'GET':
        return jsonify(retrieve())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create())
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
