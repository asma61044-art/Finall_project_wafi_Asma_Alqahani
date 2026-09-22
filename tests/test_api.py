from fastapi.testclient import TestClient
from wafi.api.app import app
c=TestClient(app)

def test_health():
    assert c.get("/health").json()=={"status":"alive"}

def test_ready():
    assert c.get("/ready").json()=={"status":"ready"}

def test_predict():
    r=c.post("/v1/predict",json={"ticket_id":"T-1","text":"VPN is slow"})
    assert r.status_code==200
    assert r.json()["team"]=="network"
    assert r.json()["urgency"]=="medium"
    assert r.json()["trace_id"]

def test_extra_field_rejected():
    assert c.post("/v1/predict",json={"ticket_id":"T-1","text":"VPN","bad":"x"}).status_code==422
