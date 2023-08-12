from main import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello to my homepage' in response.data


def test_random_name(client):
    response = client.get('/brenda')
    assert response.status_code == 200 
    assert b'Brenda' in response.data


# def test_custom_name(client):
#     response = client.post('/custom', data={'name':'brenda'})
#     assert response.status_code == 200 
#     assert b'Brenda' in response.data
