from fastapi.testclient import TestClient
from generators.week8_web_api.exercises import app


client = TestClient(app)


def test_create_and_get_item():
    resp = client.post("/items/", json={"id": 1, "name": "a"})
    assert resp.status_code == 200
    resp = client.get("/items/1")
    assert resp.status_code == 200
    assert resp.json()["name"] == "a"
