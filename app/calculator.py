# calculator.py
# This is the "Facade" - it hides the operations/history/memento stuff
# so the REPL only has to talk to one class instead of three.
# Also has the Observer stuff in here (logging + autosave)

from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.history import HistoryManager
from app.calculator_config import CalculatorConfig
from app.input_validators import validate_number, validate_operation


# Observer pattern - observers get told whenever a calculation happens
class Observer:
    def notify(self, calculation):
        raise NotImplementedError  # pragma: no cover


class LoggingObserver(Observer):
    # just prints out what happened, mostly for debugging
    def notify(self, calculation):
        print(f"LOG: {calculation.operation}({calculation.a}, {calculation.b}) = {calculation.result}")


class AutoSaveObserver(Observer):
    # this is the one the assignment talks about - auto save history
    def __init__(self, calculator):
        self.calculator = calculator

    def notify(self, calculation):
        self.calculator.save_history()


class Calculator:
    # this class is the facade - REPL should only ever call this class
    def __init__(self, config=None):
        if config is None:
            config = CalculatorConfig()
        self.config = config

        self.factory = OperationFactory()
        self.memento = CalculatorMemento()
        self.history_manager = HistoryManager(self.config.history_file)
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def calculate(self, op_name, a, b):
        op_name = validate_operation(op_name)
        a = validate_number(a)
        b = validate_number(b)

        op = self.factory.get(op_name)
        result = op.execute(a, b)

        calc = Calculation(op_name, a, b, result)

        self.memento.save(self.history_manager.history.copy())
        self.history_manager.add(calc)

        for obs in self.observers:
            obs.notify(calc)

        return result

    def undo(self):
        current = self.history_manager.history.copy()
        old_state = self.memento.undo()
        if old_state is not None:
            self.memento.redo_stack[-1].state = current
            self.history_manager.history = old_state
        return old_state

    def redo(self):
        old_state = self.memento.redo()
        if old_state is not None:
            self.history_manager.history = old_state
        return old_state

    def save_history(self):
        self.history_manager.save()

    def load_history(self):
        self.history_manager.load()

    def clear_history(self):
        self.history_manager.history = self.history_manager.history.iloc[0:0]

    def get_history(self):
        return self.history_manager.history
