# test_calculator_config.py
# tests for configuration loading and validation

import os
import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_default_values():
    os.environ.pop("MAX_HISTORY_SIZE", None)
    os.environ.pop("MAX_INPUT_VALUE", None)

    config = CalculatorConfig()

    assert config.max_history_size == 100
    assert config.max_input_value == 1_000_000
    assert config.history_file == "history.csv"


def test_custom_values():
    os.environ["MAX_HISTORY_SIZE"] = "50"
    os.environ["MAX_INPUT_VALUE"] = "5000"
    os.environ["HISTORY_FILE"] = "test.csv"

    config = CalculatorConfig()

    assert config.max_history_size == 50
    assert config.max_input_value == 5000
    assert config.history_file == "test.csv"


def test_invalid_int():
    os.environ["MAX_HISTORY_SIZE"] = "not_a_number"

    with pytest.raises(ConfigurationError):
        CalculatorConfig()


def test_negative_value():
    os.environ["MAX_HISTORY_SIZE"] = "-10"

    with pytest.raises(ConfigurationError):
        CalculatorConfig()