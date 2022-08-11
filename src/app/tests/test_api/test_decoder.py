from app.settings import API_V1_STR
from fastapi.testclient import TestClient
import pytest


@pytest.mark.parametrize("text,expected_value", [("vGFO**", 12345678), ("D5lGU*", 65425812), ("FB****", 321)])
def test_decode(client: TestClient, text, expected_value) -> None:
    response = client.get(f"{API_V1_STR}/decoder/{text}")
    content = response.json()

    assert response.status_code == 200
    assert content["decoded_value"] == expected_value


def test_encode_with_not_allowed_max_number(client: TestClient):
    response = client.get(f"{API_V1_STR}/decoder/ABCdefg")
    content = response.json()

    assert response.status_code == 422
    assert content["detail"][0]["type"] == "value_error.any_str.max_length"
