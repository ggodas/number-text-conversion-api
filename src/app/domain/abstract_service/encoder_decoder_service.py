from abc import ABC, abstractmethod

from app.domain.models.encoder_model import Encoded, Decode


class EncoderService(ABC):
    @abstractmethod
    def encode(self, number: int) -> Encoded:
        raise NotImplementedError()


class DecoderService(ABC):
    @abstractmethod
    def decode(self, text: str) -> Decode:
        raise NotImplementedError()
