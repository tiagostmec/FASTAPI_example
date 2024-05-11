from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_spectrum():
    response = client.post("/spectrum_process", json={
  "frequencies": [
    0,
    1000,
    2000,
    3000,
    4000,
    5000
  ],
  "amplitudes": [
    0.0008313103973909813,
    0.0037717779347257807,
    0.002215142872924636,
    0.0010077122629765603,
    0.001000390598006626,
    0.000504799346355255
  ]
})
    assert response.status_code == 200
    data = response.json()
    assert "status"in data
