FROM python:3.11-alpine as python-base
ENV POETRY_VERSION=1.5.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

# Stage 1: Установка Poetry
FROM python-base as poetry-base
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}


# Stage 2: Настройка приложения
FROM python-base as app
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN poetry check
RUN poetry install --no-interaction --no-cache --no-root
RUN poetry add fastapi

COPY . ./

CMD ["poetry", "run", "python", "-m", "app"]
