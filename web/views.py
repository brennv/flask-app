from flask import current_app, Blueprint
import os
import yaml
from redis import Redis  # , StrictRedis

api = Blueprint('api', __name__)


def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]


@api.route("/")
def index():
    redis = Redis(host="redis")
    # redis_url = os.environ.get('redis')
    # redis = redis.StrictRedis(host=url, port=6379, db=0)
    visits = redis.incr('counter')
    name = os.environ.get('HELLO_NAME') or load_config('name')
    html = "<h3>hello {name}</h3>" \
           "<b>visits:</b> {visits}" \
           "<br/>"
    return html.format(name=name, visits=visits)
