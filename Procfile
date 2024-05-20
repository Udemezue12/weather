
release: python manage.py makemigrations --no-input && python manage.py migrate --no-input

web: gunicorn weather_app.auth:application

web: waitress-serve --port=$PORT weather_app.wsgi:application
