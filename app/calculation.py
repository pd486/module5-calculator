# calculation.py
# stores a single calculation

from datetime import datetime


class Calculation:
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp
        }