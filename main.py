from flask import Flask, render_template
import requests
import socket

TIMEOUT = 0.1

app = Flask(__name__)

default_servers = [
    ('Reticent', 'T2', ('10.132.64.47', 80)),
    ('Saber', 'T1', ('10.132.67.8', 80)),
    ('Assassin', 'T1', ('10.132.67.81', 80))
]

default_services = [
    ('Personal Site', 'https://reticent.io'),
    ('Eevee', 'https://eevee.reticent.io'),
    ('Sniper', 'https://sniper.reticent.io/meta/sign_in'),
    ('Notepad', 'https://notepad.somoe.moe'),
    ('SoMoe', 'https://somoe.moe'),
    ('zbAction', 'http://zbaction.reticent.io'),
    ('Dashboard', 'http://saber.reticent.io')
]

def check_ip(addr):
    try:
        socket.create_connection(addr, timeout=TIMEOUT)
        return True
    except socket.error:
        return False

def check_site(addr):
    try:
        r = requests.head(addr, timeout=TIMEOUT)
        return r.status_code >= 200 and r.status_code < 300
    except:
        return False

@app.route('/')
def status():
    servers = [(x, check_ip(x[1])) for x in default_servers]
    services = [(x, check_site(x[1])) for x in default_services]

    return render_template('index.html', servers=servers, services=services)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4678, threaded=True, debug=True)
