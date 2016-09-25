from flask import Flask
# from sqlalchemy import create_engine

from .views import api


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(api)
    # app.engine = create_engine(database_uri)
    return app
