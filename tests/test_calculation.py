# test_calculation.py
# tests for Calculation class

from app.calculation import Calculation


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)

    assert calc.operation == "add"
    assert calc.a == 2
    assert calc.b == 3
    assert calc.result == 5


def test_calculation_to_dict():
    calc = Calculation("multiply", 3, 4, 12)
    data = calc.to_dict()

    assert data["operation"] == "multiply"
    assert data["a"] == 3
    assert data["b"] == 4
    assert data["result"] == 12
    assert "timestamp" in data