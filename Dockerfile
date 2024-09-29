ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /TFG

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY ./app/ ./app/
COPY ./src/ ./src/
COPY ./scripts/ ./scripts/
COPY ./data/ ./data/
COPY ./dashboard/ ./dashboard/

EXPOSE 8000

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000 --no-server-header
