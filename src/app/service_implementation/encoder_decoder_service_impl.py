import string
from app.domain.exception.exceptions import InvalidNumberException
from app.domain.models.encoder_model import Decode, Encoded
from app.domain.abstract_service.encoder_decoder_service import EncoderService, DecoderService

ALPHABET = f"{string.ascii_uppercase}{string.ascii_lowercase}{string.digits}-_"
ALPHABET_REVERSE = dict((c, i) for (i, c) in enumerate(ALPHABET))
BASE = len(ALPHABET)
FILL_CHR = "*"
SIGNED_CHR = "$"


class EncoderServiceImpl(EncoderService):
    def encode(self, number: int) -> Encoded:
        if number > 99999999:
            raise InvalidNumberException("The number must be between 0 and 99999999")

        if number < 0:
            return SIGNED_CHR + self.encode(-number).encoded_value
        s = []
        while True:
            number, r = divmod(number, BASE)
            s.append(ALPHABET[r])
            if number == 0:
                break
        res = "".join(reversed(s))
        res = res.ljust(6, FILL_CHR)
        return Encoded(res)


class DecoderServiceImpl(DecoderService):
    def decode(self, text: str) -> Decode:
        if text[0] == SIGNED_CHR:
            return -self.decode(text[1:]).decoded
        n = 0
        for c in text:
            if c == FILL_CHR:
                continue
            n = n * BASE + ALPHABET_REVERSE[c]
        return Decode(n)
