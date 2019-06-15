from impractical import app

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/palingram-spells', methods=['GET'])
def palingrams():
    return main.generate_palingram()