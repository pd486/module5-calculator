import pytest
from app.operations import OperationFactory
from app.exceptions import OperationError, DivisionByZeroError


def test_operations_work():
    f = OperationFactory()

    assert f.get("add").execute(1, 2) == 3
    assert f.get("subtract").execute(5, 3) == 2
    assert f.get("multiply").execute(2, 3) == 6
    assert f.get("divide").execute(6, 2) == 3
    assert f.get("power").execute(2, 3) == 8
    assert f.get("root").execute(16, 2) == 4


def test_unknown_operation():
    f = OperationFactory()

    with pytest.raises(OperationError):
        f.get("invalid_operation")


def test_divide_by_zero():
    f = OperationFactory()

    with pytest.raises(DivisionByZeroError):
        f.get("divide").execute(5, 0)


def test_root_of_negative():
    f = OperationFactory()

    with pytest.raises(OperationError):
        f.get("root").execute(-4, 2)