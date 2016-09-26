from flask import current_app, Blueprint, jsonify
import os
import yaml

api = Blueprint('api', __name__)


@api.route("/")
def index():
    with open('config.yml') as f:
        data = yaml.load(f)
    name = os.environ.get('HELLO_NAME') or data['name']
    return jsonify(hello=name)
