# web: uvicorn tee_backend.web.app:get_app --host=0.0.0.0 --port=80 --factory --workers=1
# web: gunicorn tee_backend.web.app:get_app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --log-file -
# web: python -m tee_backend
# web: python server.py
web: uvicorn tee_backend.web.app:app --host=0.0.0.0 --port=$PORT --workers=1
