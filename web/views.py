from flask import current_app, Blueprint
from redis import Redis, RedisError
import os
import socket
import yaml

api = Blueprint('api', __name__)


def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]


@api.route("/")
def index():
    redis = Redis(host="redis", db=0)
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "<i>redis connection error</i>"
    name = os.environ.get('HELLO_NAME') or load_config('name')
    hostname = socket.gethostname()
    html = "<h3>hello {name}</h3>" \
           "<b>host:</b> {hostname}<br/>" \
           "<b>visits:</b> {visits}"
    return html.format(name=name, hostname=hostname, visits=visits)
