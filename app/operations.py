# operations.py
# calculator operations using simple strategy + factory

from abc import ABC, abstractmethod
from app.exceptions import DivisionByZeroError, OperationError


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass  # pragma: no cover


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("cannot divide by zero")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if a < 0:
            raise OperationError("invalid root operation")
        return a ** (1 / b)


class OperationFactory:
    def __init__(self):
        self.ops = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "root": Root()
        }

    def get(self, name):
        if name not in self.ops:
            raise OperationError(f"unknown operation: {name}")
        return self.ops[name]