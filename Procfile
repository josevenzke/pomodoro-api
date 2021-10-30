web: gunicorn --pythonpath pomodoro pomodoro.wsgi
release: python pomodoro/manage.py makemigrations
release: python pomodoro/manage.py migrate