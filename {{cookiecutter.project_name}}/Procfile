web: gunicorn config.wsgi --log-file -
# web: daphne config.asgi:application --bind 0.0.0.0 --port ${PORT}
release: python manage.py migrate && python manage.py cleandata
