[![Python](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6--dev-blue.svg)]()
[![Requirements](https://requires.io/github/brennv/flask-app/requirements.svg?branch=master)](https://requires.io/github/brennv/flask-app/requirements/?branch=master)
[![Travis](https://travis-ci.org/brennv/flask-app.svg?branch=master)](https://travis-ci.org/brennv/flask-app)
[![Coverage](https://codecov.io/gh/brennv/flask-app/branch/master/graph/badge.svg)](https://codecov.io/gh/brennv/flask-app)
[![Code Climate](https://codeclimate.com/github/brennv/flask-app/badges/gpa.svg)](https://codeclimate.com/github/brennv/flask-app)
[![Docker](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg?maxAge=2592000)]()

# flask-app

Example app for testing continuous integration workflows.

## Getting started

`docker compose up`

Visit [http://localhost:5000](http://localhost:5000)

## Development

After making changes rebuild images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
# docker stop flaskapp_redis_1
```

## Tests

Tests run with:

```shell
docker-compose -f docker-compose.test -p ci build
docker-compose -f docker-compose.test -p ci run \
    test python -m pytest --cov=web/ tests
# docker stop ci_web_1 ci_redis_1
```

## Automated tests

Pull requests tested via [travis-ci.org](https://travis-ci.org/brennv/flask-app).
Coverage reported to [codecov.io](https://codecov.io/gh/brennv/flask-app).

## Automated builds and redeploys

Registry images automatically built from repo branch changes. New registry
images are automatically redeployed to staging and production.

Image tagging scheme:

- `flask-app:latest` follows the `master` branch for **production**
- `flask-app:develop` follows the `develop` branch for **staging**

Version tags, like `flask-app:v0.2`, follow repo release tags.

## Notifications

Updates pushed via Slack project channel for:

- github
- travis-ci
- docker cloud
