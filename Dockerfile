FROM python:3.10

ARG IS_DEVELOPMENT

RUN pip install 'poetry==1.0'

WORKDIR /usr/app/
COPY poetry.lock pyproject.toml /usr/app/
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$IS_DEVELOPMENT" != 1 && echo "--no-dev") --no-interaction --no-ansi

COPY . /usr/app/
ENV FLASK_APP=/usr/app/src/application/flask_app.py \
    FLASK_DEBUG=${IS_DEVELOPMENT:-0} \
    PYTHONUNBUFFERED=1
CMD flask run --host=0.0.0.0 --port=80
