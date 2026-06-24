# test_input_validators.py

import pytest
from app.input_validators import validate_number, validate_operation
from app.exceptions import ValidationError


def test_validate_number_valid():
    assert validate_number("10") == 10.0


def test_validate_number_invalid():
    with pytest.raises(ValidationError):
        validate_number("abc")


def test_validate_operation_valid():
    assert validate_operation("add") == "add"


def test_validate_operation_invalid():
    with pytest.raises(ValidationError):
        validate_operation("invalid_op")