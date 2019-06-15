import flask
from flask import request, jsonify
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/anagram-solver/<string:keyword>', methods=['GET'])
def anagrams(keyword):
    return main.generate_anagrams(keyword)

app.run()