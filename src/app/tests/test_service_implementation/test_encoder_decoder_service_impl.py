import pytest


@pytest.mark.parametrize("number,expected_value", [(12345678, "vGFO**"), (65425812, "D5lGU*"), (321, "FB****")])
def test_encoder_service_impl(encoder_service_impl, number: int, expected_value: str):
    assert encoder_service_impl.encode(number).encoded_value == expected_value


@pytest.mark.parametrize("text,expected_value", [("vGFO**", 12345678), ("D5lGU*", 65425812), ("FB****", 321)])
def test_decoder_service_impl(decoder_service_impl, text: str, expected_value: int):
    assert decoder_service_impl.decode(text).decoded_value == expected_value
