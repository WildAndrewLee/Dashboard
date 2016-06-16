from flask import Flask, render_template
import json
from object import Object

app = Flask(__name__)

TIMEOUT = 0.2

@app.route('/')
def status():
    with open('/var/www/Dashboard/status.json') as f:
        status = json.loads(f.read())
        return render_template('index.html', status=Object(status))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4678, threaded=False, debug=True)
