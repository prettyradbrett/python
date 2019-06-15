from flask import Flask
from flask import request, jsonify

import impractical.views.views

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()