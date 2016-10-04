import os
import socket
from flask import Blueprint
from .db import redis, RedisError
import yaml

api = Blueprint('api', __name__)


def load_config(value):
    with open('config.yml') as f:
        data = yaml.load(f)
    return data[value]


@api.route("/")
def index():
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
