from unittest.mock import patch
import pandas as pd
from app import calculator_repl


def run_with_inputs(inputs, history_file):
    import os
    os.environ["MAX_HISTORY_SIZE"] = "100"
    os.environ["MAX_INPUT_VALUE"] = "1000000"
    pd.DataFrame(columns=["operation", "a", "b", "result", "timestamp"]).to_csv(history_file, index=False)
    inputs_iter = iter(inputs + ["exit"])
    with patch("builtins.input", lambda *_: next(inputs_iter)):
        calculator_repl.run()


def test_repl_add(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 2 3"], history_file)
    out = capsys.readouterr().out
    assert "result: 5" in out


def test_repl_empty_input(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs([""], history_file)
    out = capsys.readouterr().out
    assert "Calculator REPL" in out


def test_repl_help(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["help"], history_file)
    out = capsys.readouterr().out
    assert "commands:" in out


def test_repl_history(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1 1", "history"], history_file)
    out = capsys.readouterr().out
    assert "operation" in out


def test_repl_undo_nothing(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["undo"], history_file)
    out = capsys.readouterr().out
    assert "nothing to undo" in out


def test_repl_undo_something(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1 1", "undo"], history_file)
    out = capsys.readouterr().out
    assert "undone" in out


def test_repl_redo_nothing(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["redo"], history_file)
    out = capsys.readouterr().out
    assert "nothing to redo" in out


def test_repl_redo_something(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1 1", "undo", "redo"], history_file)
    out = capsys.readouterr().out
    assert "redone" in out


def test_repl_save(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1 1", "save"], history_file)
    out = capsys.readouterr().out
    assert "saved" in out


def test_repl_load(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["load"], history_file)
    out = capsys.readouterr().out
    assert "loaded" in out


def test_repl_clear(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1 1", "clear"], history_file)
    out = capsys.readouterr().out
    assert "history cleared" in out


def test_repl_invalid_format(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["add 1"], history_file)
    out = capsys.readouterr().out
    assert "invalid input" in out


def test_repl_calculation_error(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs(["divide 1 0"], history_file)
    out = capsys.readouterr().out
    assert "error:" in out


def test_repl_exit(tmp_path, monkeypatch, capsys):
    history_file = str(tmp_path / "history.csv")
    monkeypatch.setenv("HISTORY_FILE", history_file)
    run_with_inputs([], history_file)
    out = capsys.readouterr().out
    assert "bye" in out
