FROM python:3.10

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE "src.settings"

WORKDIR /app

COPY ./recommendations .

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["gunicorn", "src.wsgi"]