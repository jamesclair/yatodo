ARG DESTINATION=dev

FROM python:3.12.1-slim AS base

# Trade-off w/ venv = no polution of system python/poetry
# w/o venv = performance boost 
# my answer start w/ 2, if issue switch to 1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

# pin the package manager's version
RUN pip install poetry==1.5.1

COPY ./pyproject.toml ./poetry.lock* /code/

FROM base AS prod
# cache the poetry deps, may cause issue in CI
# no dev deps
# don't install the app
RUN  --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root

FROM base AS dev

RUN  --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --with dev --no-root

COPY ./.env /code/.env
# Copy only what you want
# This should be as close to end as possible as it will change too often to use cache.

FROM ${DESTINATION}

COPY ./src /code/app

# install the app
RUN poetry install --only-root

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
