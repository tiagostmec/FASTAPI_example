from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_spectrum():
    """
    Test the /spectrum endpoint for different scenarios.
    - Check if the endpoint returns status 200.
    - Check if the returned data has the expected format.
    - Verify if the endpoint returns valid values for the specific parameters nperseg = 1024 and window = 'hann'.
    - Check if the data types of the return values are correct.
    - Verify the behavior for no parameters provided.
    - Verify the behavior for extreme parameter values.
    - Verify the behavior for invalid parameter values.
    """
    # Test
    response = client.get("/spectrum/?nperseg=1024&window=hann")
    assert response.status_code == 200
    data = response.json()
    assert "frequencies" in data
    assert "amplitudes" in data
    assert len(data["frequencies"]) == 513  # nperseg/2 + 1
    assert len(data["amplitudes"]) == 513

    # Check if the data types of the return values are correct.
    assert isinstance(data["status"], str)
    assert isinstance(data["frequencies"], list)
    assert isinstance(data["amplitudes"], list)

    # Verify the behavior for no parameters provided.
    response = client.get("/spectrum/")
    assert response.status_code == 422

    # Verify the behavior for extreme parameter values.
    response = client.get("/spectrum/?nperseg=1&window=hann")
    assert response.status_code == 200
    data = response.json()
    assert len(data["frequencies"]) == 1
    assert len(data["amplitudes"]) == 1

    response = client.get("/spectrum/?nperseg=100000&window=hann")
    assert response.status_code == 200
    data = response.json()
    assert len(data["frequencies"]) == 50001
    assert len(data["amplitudes"]) == 50001

    # Verify the behavior for invalid parameter values
    response = client.get("/spectrum?nperseg=-1&window=hann")
    assert response.status_code == 422
    response = client.get("/spectrum?nperseg=1024&window=invalid")
    assert response.status_code == 422