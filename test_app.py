# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'CI/CD 演示成功' in response.json['message']

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'