from app.settings import API_V1_STR
from fastapi.testclient import TestClient
import pytest


@pytest.mark.parametrize("number,expected_value", [(12345678, "vGFO**"), (65425812, "D5lGU*"), (321, "FB****")])
def test_encode(client: TestClient, number, expected_value) -> None:
    response = client.get(f"{API_V1_STR}/encoder/{number}")
    content = response.json()

    assert response.status_code == 200
    assert content["encoded_value"] == expected_value


def test_encode_with_not_allowed_max_number(client: TestClient):
    response = client.get(f"{API_V1_STR}/encoder/123456789")
    content = response.json()

    assert response.status_code == 422
    assert content["detail"][0]["type"] == "value_error.number.not_le"
