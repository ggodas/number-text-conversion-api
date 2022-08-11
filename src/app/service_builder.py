import logging

from app.domain.abstract_service.encoder_decoder_service import EncoderService, DecoderService
from app.service_implementation.encoder_decoder_service_impl import DecoderServiceImpl, EncoderServiceImpl


def get_encoder_service_builder(param=None) -> EncoderService:
    logging.warning(param)
    return EncoderServiceImpl()


def get_decoder_service_builder() -> DecoderService:
    return DecoderServiceImpl()
