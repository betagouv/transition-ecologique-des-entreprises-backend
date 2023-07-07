# tee_backend

This project was generated using [fastapi_template](https://github.com/topics/fastapi-boilerplate).

---

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
# poetry run python -m tee_backend
poetry run python server.py
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

To export requirements run:

```bash
poetry export -f requirements.txt --without-hashes --output requirements.txt
```

---

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

---

## Project structure

```bash
$ tree "tee_backend"
tee_backend
├── conftest.py  # Fixtures for all tests.
├── server.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── app.py  # FastAPI application configuration.
    ├── app_factory.py  # FastAPI application configuration for factory mode.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "TEE_BACKEND_" prefix.

For example if you see in your "tee_backend/settings.py" a variable named like
`random_parameter`, you should provide the "TEE_BACKEND_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `tee_backend.settings.Settings.Config`.

An example of .env file:

```bash
TEE_BACKEND_RELOAD="True"
TEE_BACKEND_PORT="8000"
TEE_BACKEND_ENVIRONMENT="dev"
TEE_BACKEND_LOG_LEVEL="DEBUG"
TEE_BACKEND_TOKEN_API_BREVO="xxxx"
TEE_BACKEND_TOKEN_API_SIREN="xxxx"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

---

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);

You can read more about pre-commit here: https://pre-commit.com/

## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.


2. Run the pytest.
```bash
pytest -vv .
```

---

## Deploy on Scalingo

### Procfile

Scalingo needs a `Procfile`with :

- At least one `web: ...` entry
- `host` must be set on `0.0.0.0`
- `port` must use the automatic port provided by Scalingo, so it needs to be set on `$PORT`

```
web: uvicorn tee_backend.web.app:app --host=0.0.0.0 --port=$PORT --workers=1
```

### Requirements.txt

Export a `requirements.txt` from poetry

```
poetry export --without-hashes --without dev --format=requirements.txt > requirements.txt
```
