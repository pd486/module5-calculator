from app.calculator_memento import CalculatorMemento

def test_full_memento_flow():
    m = CalculatorMemento()

    m.save("a")
    m.save("b")

    assert m.can_undo()
    assert m.undo() == "b"
    assert m.undo() == "a"
    assert m.undo() is None

    assert m.can_redo()
    assert m.redo() == "a"
    assert m.redo() == "b"


def test_empty_memento():
    m = CalculatorMemento()

    assert m.undo() is None
    assert m.redo() is None
