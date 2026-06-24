# Enhanced Calculator Application

A command-line calculator built with Python, featuring design patterns, pandas-based history management, and full test coverage.

## Features

- REPL interface for continuous interaction
- Arithmetic operations: add, subtract, multiply, divide, power, root
- Undo/redo support
- Auto-saving calculation history to CSV using pandas
- Configurable via environment variables (.env file)

## Design Patterns Used

- Factory - OperationFactory creates the correct operation class based on user input (app/operations.py)
- Strategy - each operation implements a shared interface, making them interchangeable (app/operations.py)
- Memento - CalculatorMemento stores history snapshots to support undo/redo (app/calculator_memento.py)
- Observer - LoggingObserver and AutoSaveObserver react to every calculation event (app/calculator.py)
- Facade - the Calculator class wraps the factory, history manager, and memento behind one simple interface (app/calculator.py)

## Setup

1. Clone the repository: git clone https://github.com/pd486/module5-calculator.git then cd module5_calculator
2. Create and activate a virtual environment: python3 -m venv venv then source venv/bin/activate
3. Install dependencies: pip install pandas python-dotenv pytest pytest-cov
4. Optionally create a .env file with MAX_HISTORY_SIZE=100, MAX_INPUT_VALUE=1000000, HISTORY_FILE=history.csv

## Usage

Run the calculator with: python -m app.calculator_repl

Commands: add/subtract/multiply/divide/power/root num1 num2 to calculate, history to view past calculations, undo and redo to step back and forward, save and load for the CSV file, clear to wipe history, help to list commands, exit to quit.

## Error Handling

EAFP is used in history.py and operations.py via try/except. LBYL is used in input_validators.py, checking the operation name is valid before using it.

## Testing

Run pytest --cov=app tests/ to run the full suite with coverage. This project maintains 100% test coverage, enforced via GitHub Actions on every push.

## Continuous Integration

GitHub Actions (.github/workflows/python-app.yml) runs the test suite and checks for 100% coverage on every push and pull request to main.
