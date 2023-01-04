import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_welcome_page(client):
    response = client.get('/')
    assert b"<body>Bienvenue sur Football Stats</body>" in response.data

def test_teams(client):
    response = client.get('/teams')
    assert response.status_code == 200
    
def test_players(client):
    response = client.get('/players')
    assert response.status_code == 200