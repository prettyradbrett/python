import flask
from flask import request, jsonify
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True

palingram_response = main.generate_palingram()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/palingram-spells', methods=['GET'])
def palingrams():
    return palingram_response

app.run()