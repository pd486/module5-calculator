import pytest
import pandas as pd
from app.history import HistoryManager
from app.calculation import Calculation


def test_history_save_and_load(tmp_path):
    file = tmp_path / "history.csv"
    h = HistoryManager(str(file))

    c = Calculation("add", 1, 2, 3)
    h.add(c)

    h.save()
    h.load()

    assert len(h.history) >= 1


def test_history_load_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise Exception("fail")

    monkeypatch.setattr(pd, "read_csv", fail)

    h = HistoryManager("fake.csv")

    with pytest.raises(Exception):
        h.load()


def test_history_add_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise Exception("fail")

    monkeypatch.setattr(pd, "concat", fail)

    h = HistoryManager("fake.csv")
    c = Calculation("add", 1, 2, 3)

    with pytest.raises(Exception):
        h.add(c)


def test_history_save_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise Exception("fail")

    monkeypatch.setattr(pd.DataFrame, "to_csv", fail)

    h = HistoryManager("fake.csv")

    with pytest.raises(Exception):
        h.save()