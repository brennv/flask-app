from flask import Flask
# from redis import Redis

from .views import api, load_config


def create_app(debug=False):
    # redis = Redis(host="redis", db=0)
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(api)
    return app
