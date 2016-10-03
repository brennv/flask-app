FROM python:3-alpine

RUN apk add --update bash curl git && rm -rf /var/cache/apk/*

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN pip install pytest pytest-cov pytest-flask

# RUN python -m pytest --cov=web/ tests
