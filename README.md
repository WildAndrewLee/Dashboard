Dashboard
===
A flexible server/service availability dashboard.

For best results set a cronjob to run `check.py` every minute.

Running Dashboard
===
Before you run Dashboard `check.py` must be run at least once. If you've already run `check.py` and a `status.json` file has been created then all you need to do is run `main.py`. Dashboard will use port 4678 by default however you can change it in your `config.json` file.

You can also run Dashboard through Gunicorn and uWSGI.

Adding Servers/Services
===

All servers and services to be checked are managed by the `checklist.json` file. A server/service to check will take the form:
```
{
    "name": "Required",
    "type": "Optional",
    "ip": "Optional",
    "port": "Required If IP Used (this should be an int not a string)"
    "url": "Optional"
}
```
Note that you are required to have either a URL or IP (and port) specified. In the event that you specify both, the URL will be checked first. If the URL is not available then the IP will be used as a fallback.
