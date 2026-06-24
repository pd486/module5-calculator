# exceptions.py
# custom exceptions for calculator errors

class CalculatorError(Exception):
    pass


class ValidationError(CalculatorError):
    pass


class OperationError(CalculatorError):
    pass


class DivisionByZeroError(OperationError):
    pass


class ConfigurationError(CalculatorError):
    pass


class HistoryError(CalculatorError):
    pass