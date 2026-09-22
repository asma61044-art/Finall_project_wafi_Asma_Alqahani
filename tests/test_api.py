from fastapi.testclient import TestClient

from wafi.api.app import app


def test_health():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "alive"}


def test_ready():
    with TestClient(app) as client:
        assert client.get("/ready").json() == {"status": "ready"}


def test_predict():
    with TestClient(app) as client:
        r = client.post("/v1/predict", json={"ticket_id": "T-1", "text": "VPN is slow"})
        assert r.status_code == 200
        assert r.json()["team"] == "network"
        assert r.json()["urgency"] == "medium"
        assert r.json()["trace_id"]
        assert r.json()["reason"] == "standard keyword policy"


def test_extra_field_rejected():
    with TestClient(app) as client:
        assert client.post(
            "/v1/predict",
            json={"ticket_id": "T-1", "text": "VPN", "bad": "x"},
        ).status_code == 422
