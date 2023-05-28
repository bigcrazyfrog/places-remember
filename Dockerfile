FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN apt-get update && \
    python -m pip install --upgrade pip && \
    pip install pipenv
RUN pipenv install --system --deploy

COPY . /code