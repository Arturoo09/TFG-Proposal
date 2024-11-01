ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /TFG

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app/ ./app/
COPY ./src/ ./src/
COPY ./scripts/ ./scripts/
COPY ./data/ ./data/
COPY ./modules/ ./modules/
COPY ./dashboard/ ./dashboard/

ENV PYTHONPATH="${PYTHONPATH}:/TFG"

EXPOSE 8000

CMD ["uvicorn", "app.src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--no-server-header"]
