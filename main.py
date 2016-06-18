from flask import Flask, render_template
import json
from object import Object
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

with open(os.path.join(CURRENT_DIR, 'config.json')) as f:
    config = Object(json.loads(f.read()))

@app.route('/')
def status():
    with open(os.path.join(CURRENT_DIR, 'status.json')) as f:
        status = json.loads(f.read())
        return render_template('index.html', status=Object(status))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.port, threaded=False, debug=True)
