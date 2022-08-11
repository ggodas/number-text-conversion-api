from typing import Union
from operator import lt
from fastapi import APIRouter, Depends, Path

from app.domain.models.encoder_model import Encoded
from app.service_builder import get_encoder_service_builder
from app.domain.abstract_service.encoder_decoder_service import EncoderService

encoder_route = APIRouter()

number_validation = Path(title="The number must be between 0 and 99999999", ge=0, le=99999999)
depends = Depends(get_encoder_service_builder)


@encoder_route.get("/{number}", response_model=Encoded)
def encode_number(number: int = number_validation, encoder_service: EncoderService = depends):  # noqa
    encoded_result = encoder_service.encode(number)
    return encoded_result
