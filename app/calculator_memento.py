# calculator_memento.py
# handles undo and redo functionality (memento pattern)

class Memento:
    def __init__(self, state):
        self.state = state


class CalculatorMemento:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        self.undo_stack.append(Memento(state))
        self.redo_stack.clear()

    def undo(self):
        if len(self.undo_stack) == 0:
            return None

        memento = self.undo_stack.pop()
        self.redo_stack.append(memento)
        return memento.state

    def redo(self):
        if len(self.redo_stack) == 0:
            return None

        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento.state

    def can_undo(self):
        return len(self.undo_stack) > 0

    def can_redo(self):
        return len(self.redo_stack) > 0