from dataclasses import dataclass


@dataclass
class Encoded(object):
    encoded_value: str


@dataclass
class Decode(object):
    decoded_value: int
