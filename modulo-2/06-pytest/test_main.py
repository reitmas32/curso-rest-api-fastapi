from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola desde FastAPI"}


def test_suma():
    response = client.get("/suma?a=3&b=4")
    assert response.status_code == 200
    assert response.json() == {"resultado": 7}


def test_suma_negativos():
    response = client.get("/suma?a=-2&b=-5")
    assert response.status_code == 200
    assert response.json() == {"resultado": -7}
