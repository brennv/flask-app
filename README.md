# flask-app

Example app for testing continuous integration workflows.

## Getting started

Install the requirements and run the app.

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## Tests

Tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=example/ tests
```

## Automated tests

Pull requests tested on [travis-ci.org](https://travis-ci.org/brennv/flask-app). Coverage reported to [codecov.io](https://codecov.io/gh/brennv/flask-app).

## Containerized

Build and run the app as a docker image.

```shell
docker build -t flask-app .
docker run -it -p 5000:5000 --rm --name flask-app flask-app
```
