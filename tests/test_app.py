import os
from flask import Flask, url_for
import pytest
import yaml

from example import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_app(client):
    response = client.get(url_for('api.index'))
    assert response.status_code == 200
    with open('config.yml') as f:
        data = yaml.load(f)
    name = os.environ.get('HELLO_NAME') or data['name']
    assert response.json == {'hello': name}
    assert response.json != {'hello': 'fail'}
