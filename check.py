import requests
import socket
import json
import os
from object import Object

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_DIR, 'checklist.json')) as checklist:
    with open(os.path.join(CURRENT_DIR, 'config.json')) as config:
        checklist = Object(json.loads(checklist.read()))
        config = Object(json.loads(config.read()))

def check_ip(addr):
    try:
        socket.create_connection(addr, timeout=config.timeout)
        return True
    except socket.error:
        return False

def check_site(addr):
    try:
        r = requests.head(addr, timeout=config.timeout)
        return r.status_code >= 200 and r.status_code < 300
    except:
        return False

for category in checklist.checklist:
    l = category.list

    for to_check in l:
        if hasattr(to_check, 'url'):
            to_check.status = check_site(to_check.url)
        elif not getattr(to_check, 'status', False) and hasattr(to_check, 'ip') and hasattr(to_check, 'port'):
            to_check.status = check_ip((to_check.ip, to_check.port))
        else:
            raise AttributeError

to_dump = {
    'checklist': []
}

for category in checklist.checklist:
    to_dump['checklist'].append({
        'category': category.category,
        'list': [
            x.__dict__ for x in category.list
        ]
    })

with open(os.path.join(CURRENT_DIR, 'status.json'), 'w+') as f:
    f.write(json.dumps(to_dump))
