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
        return 1
    except socket.timeout:
        try:
            socket.create_connection(addr, timeout=config.timeout + 0.5);
            return 2
        except socket.timeout:
            return 0
    except socket.error:
        return 0

def check_site(addr):
    try:
        r = requests.head(addr, timeout=config.timeout)

        if r.status_code >= 200 and r.status_code < 300:
            return 1
        else:
            return 0
    except requests.exceptions.Timeout:
        try:
            r = requests.head(addr, timeout=config.timeout + 0.5);
            return 2
        except requests.exceptions.Timeout:
            return 0
    except:
        return 0

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
