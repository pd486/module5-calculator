# input_validators.py
# simple validation helpers for calculator inputs

from app.exceptions import ValidationError


def validate_number(value):
    try:
        num = float(value)
    except ValueError:
        raise ValidationError("input must be a number")

    return num


def validate_operation(op):
    valid_ops = ["add", "subtract", "multiply", "divide", "power", "root"]

    if op not in valid_ops:
        raise ValidationError(f"invalid operation: {op}")

    return op