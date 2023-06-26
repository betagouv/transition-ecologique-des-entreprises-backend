FROM python:3.9.6-slim-buster as prod


RUN pip install poetry==1.4.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install --only main

# Copying actuall application
COPY . /app/src/
RUN poetry install --only main

CMD ["/usr/local/bin/python", "-m", "tee_backend"]

FROM prod as dev

RUN poetry install
