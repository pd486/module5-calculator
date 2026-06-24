import pytest
import pandas as pd
from app.calculator import Calculator, Observer, LoggingObserver, AutoSaveObserver
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError


def make_calc(tmp_path):
    file = tmp_path / "history.csv"
    config = CalculatorConfig()
    config.history_file = str(file)
    return Calculator(config)


def test_calculate_add(tmp_path):
    calc = make_calc(tmp_path)
    result = calc.calculate("add", "2", "3")
    assert result == 5


def test_calculate_invalid_operation(tmp_path):
    calc = make_calc(tmp_path)
    with pytest.raises(ValidationError):
        calc.calculate("notarealop", "2", "3")


def test_calculate_invalid_number(tmp_path):
    calc = make_calc(tmp_path)
    with pytest.raises(ValidationError):
        calc.calculate("add", "abc", "3")


def test_default_config(monkeypatch, tmp_path):
    file = tmp_path / "history.csv"
    monkeypatch.setenv("HISTORY_FILE", str(file))
    calc = Calculator()
    assert calc.config is not None


def test_undo_redo(tmp_path):
    calc = make_calc(tmp_path)
    calc.calculate("add", "2", "3")
    calc.calculate("add", "10", "10")
    assert len(calc.get_history()) == 2
    calc.undo()
    assert len(calc.get_history()) == 1
    calc.redo()
    assert len(calc.get_history()) == 2


def test_undo_with_nothing_to_undo(tmp_path):
    calc = make_calc(tmp_path)
    result = calc.undo()
    assert result is None


def test_redo_with_nothing_to_redo(tmp_path):
    calc = make_calc(tmp_path)
    result = calc.redo()
    assert result is None


def test_save_and_load_history(tmp_path):
    calc = make_calc(tmp_path)
    calc.calculate("add", "2", "3")
    calc.save_history()
    calc.load_history()
    assert len(calc.get_history()) >= 1


def test_clear_history(tmp_path):
    calc = make_calc(tmp_path)
    calc.calculate("add", "2", "3")
    calc.clear_history()
    assert len(calc.get_history()) == 0


def test_get_history(tmp_path):
    calc = make_calc(tmp_path)
    calc.calculate("add", "2", "3")
    history = calc.get_history()
    assert isinstance(history, pd.DataFrame)


def test_add_observer_and_notify(tmp_path):
    calc = make_calc(tmp_path)

    class FakeObserver(Observer):
        def __init__(self):
            self.called = False

        def notify(self, calculation):
            self.called = True

    obs = FakeObserver()
    calc.add_observer(obs)
    calc.calculate("add", "1", "1")
    assert obs.called is True


def test_logging_observer(tmp_path, capsys):
    calc = make_calc(tmp_path)
    calc.add_observer(LoggingObserver())
    calc.calculate("add", "1", "1")
    captured = capsys.readouterr()
    assert "LOG" in captured.out


def test_autosave_observer(tmp_path):
    calc = make_calc(tmp_path)
    calc.add_observer(AutoSaveObserver(calc))
    calc.calculate("add", "1", "1")
    import os
    assert os.path.exists(calc.config.history_file)


def test_observer_notify_not_implemented():
    obs = Observer()
    with pytest.raises(NotImplementedError):
        obs.notify(None)
