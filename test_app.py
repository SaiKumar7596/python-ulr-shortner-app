import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"URL Shortener Running" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_shorten_url(client):
    response = client.post('/shorten', json={
        "url": "https://google.com"
    })

    assert response.status_code == 201
    data = response.get_json()

    assert "short_code" in data
    assert "short_url" in data

def test_redirect(client):
    # First create short URL
    response = client.post('/shorten', json={
        "url": "https://google.com"
    })

    data = response.get_json()
    code = data["short_code"]

    # Now test redirect
    response = client.get(f'/{code}')
    assert response.status_code == 302  # redirect
