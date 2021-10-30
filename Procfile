web: gunicorn pomodoro.wsgi
release: python pomodoro/manage.py makemigrations --noinput
release: python pomodoro/manage.py migrate --noinput