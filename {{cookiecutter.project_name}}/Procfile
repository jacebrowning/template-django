web: gunicorn config.asgi --bind 0.0.0.0:${PORT:-5000} --worker-class uvicorn.workers.UvicornWorker --max-requests ${MAX_REQUESTS:-0} --max-requests-jitter ${MAX_REQUESTS_JITTER:-0} --timeout 25
release: python manage.py migrate && python manage.py cleandata
