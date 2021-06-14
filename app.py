from flask import Flask, jsonify, make_response
from os import environ as env

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello, world'

@app.route('/health')
def health():
  status = jsonify(status='OK',api_version=env['API_VERSION'])
  return make_response(status, 200)

@app.route('/hello')
def hello():
  status = jsonify(msg='¡Hola Mundo!')
  return make_response(status, 200)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
