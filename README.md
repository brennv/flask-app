[![Python](https://img.shields.io/badge/python-2.7%2C%203.5%2C%203.6--dev-blue.svg)]()
[![Requirements](https://requires.io/github/brennv/flask-app/requirements.svg?branch=master)](https://requires.io/github/brennv/flask-app/requirements/?branch=master)
[![Travis](https://travis-ci.org/brennv/flask-app.svg?branch=master)](https://travis-ci.org/brennv/flask-app)
[![Coverage](https://codecov.io/gh/brennv/flask-app/branch/master/graph/badge.svg)](https://codecov.io/gh/brennv/flask-app)
[![Code Climate](https://codeclimate.com/github/brennv/flask-app/badges/gpa.svg)](https://codeclimate.com/github/brennv/flask-app)
[![Docker](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg?maxAge=2592000)]()

# flask-app

Example app for demonstrating continuos integration/continuos deployment (CI/CD) workflows with docker. The example flask app connects to a [redis](http://redis.io/) instance and displays a simple visit counter and the hostname of the docker container serving the app.

## Getting started

Install [docker](https://docs.docker.com/engine/installation/) and run:

```shell
docker-compose up
# docker-compose stop
```

Otherwise, for the standalone web service:

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## Development

Create a new branch off the **develop** branch.

After making changes rebuild images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
# docker stop flaskapp_redis_1
```

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```

Integration and unit tests run with:

```shell
docker-compose -f test.yml -p ci build
docker-compose -f test.yml -p ci run test python -m pytest --cov=web/ tests
# docker stop ci_redis_1 ci_web_1
```

Commits tested via [travis-ci.org](https://travis-ci.org/brennv/flask-app). Coverage reported to [codecov.io](https://codecov.io/gh/brennv/flask-app). Code quality reported via [codeclimate.com](https://codeclimate.com/github/brennv/flask-app). Requirements inspected with [requires.io](https://requires.io/github/brennv/flask-app/requirements).

After testing submit a pull request to merge your feature or fix branch with **develop**.

## Builds and redeploys

Docker images are automatically built from changes to repo branches and tags via [docker hub autobuilds](https://docs.docker.com/docker-hub/github/). Using a cluster provisioned on [docker cloud](https://cloud.docker.com/), services are deployed as stacks from `stack/` to nodes tagged *infra* or *compute*. Setting stack option `autoredeploy: true` automatically redeploys fresh images from recent commits.

Image tagging and redeployment scheme:

- `flask-app:latest` follows the **master** branch and deploys the *latest stable release* to **production** at [http://flask-app.beta.build](http://flask-app.beta.build)
- `flask-app:develop` follows the **develop** branch and deploys to **staging** at [http://staging.flask-app.beta.build](http://staging.flask-app.beta.build)

To create sites at subdomains using virtual hosts as shown in `stack/`, assumes domain records have been configured with a `CNAME` record from `*` to `example.com.` and an `A` record from `@` to a floating IP pointing of the load balancer.

## Monitoring, log aggregation and scaling

Agent containers by [sematext](https://github.com/sematext/sematext-agent-docker) deployed to each node. Alert thresholds trigger web hooks to scale services under load.

## Notifications

Updates and alerts pushed via Slack:

- github
- travis-ci
- docker
- sematext
