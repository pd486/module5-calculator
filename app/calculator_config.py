# calculator_config.py
# loads configuration values from environment variables (.env file)

import os
from dotenv import load_dotenv
from app.exceptions import ConfigurationError

load_dotenv()


class CalculatorConfig:
    def __init__(self):
        self.max_history_size = self._get_int("MAX_HISTORY_SIZE", 100)
        self.max_input_value = self._get_int("MAX_INPUT_VALUE", 1_000_000)

        self.history_file = os.getenv("HISTORY_FILE", "history.csv")

    def _get_int(self, key, default):
        value = os.getenv(key, str(default))

        try:
            value = int(value)
        except ValueError:
            raise ConfigurationError(f"{key} must be an integer")

        if value <= 0:
            raise ConfigurationError(f"{key} must be greater than 0")

        return value