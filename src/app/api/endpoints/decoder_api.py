from typing import Union
from fastapi import APIRouter, Depends, Path

from app.domain.models.encoder_model import Decode
from app.service_builder import get_decoder_service_builder
from app.domain.abstract_service.encoder_decoder_service import DecoderService

decoder_route = APIRouter()

text_validation = Path(default=None, min_length=1, max_length=6, regex="^[a-zA-Z0-9!@#$%+*()|\-_=^/?]*$")  # noqa: W605
depends = Depends(get_decoder_service_builder)


@decoder_route.get("/{text}", response_model=Decode)
def encode_number(text: Union[str, None] = text_validation, decoder_service: DecoderService = depends):  # noqa
    decoded_result = decoder_service.decode(text)
    return decoded_result
