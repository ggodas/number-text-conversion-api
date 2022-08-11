import pytest
from typing import Generator
from fastapi.testclient import TestClient
from app.main import app
from app.service_implementation.encoder_decoder_service_impl import EncoderServiceImpl, DecoderServiceImpl


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def encoder_service_impl():
    return EncoderServiceImpl()


@pytest.fixture(scope="module")
def decoder_service_impl():
    return DecoderServiceImpl()
