# web: uvicorn tee_backend_test.web.application:get_app --host=0.0.0.0 --port=80 --factory --workers=1
web: gunicorn tee_backend_test.web.application:get_app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --log-file -
