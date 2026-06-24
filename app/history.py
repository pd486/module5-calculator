import pandas as pd
from app.exceptions import HistoryError


class HistoryManager:
    def __init__(self, file_name="history.csv"):
        self.file_name = file_name
        self.history = pd.DataFrame(columns=[
            "operation", "a", "b", "result", "timestamp"
        ])

    def add(self, calculation):
        try:
            self.history = pd.concat([
                self.history,
                pd.DataFrame([calculation.to_dict()])
            ], ignore_index=True)
        except Exception:
            raise HistoryError("failed to add calculation")

    def save(self):
        try:
            self.history.to_csv(self.file_name, index=False)
        except Exception:
            raise HistoryError("failed to save history")

    def load(self):
        try:
            self.history = pd.read_csv(self.file_name)
        except Exception:
            raise HistoryError("failed to load history")