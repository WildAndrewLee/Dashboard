Dashboard
===
A flexible server/service availability dashboard.

For best results set a cronjob to run `check.py` every minute.

Running Dashboard
===
Before you run Dashboard `check.py must be run at least once. If you've already run `check.py` and a `status.json` file has been created then all you need to do is run `main.py`. Dashboard will use port 4678 by default however you can change it in your `config.json` file.

You can also run Dashboard through Gunicorn and uWSGI.
