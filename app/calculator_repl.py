# calculator_repl.py
# this is the REPL loop, basically the main menu/cli for the calculator
# everything goes through Calculator so this file doesnt touch operations or history directly

from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.exceptions import CalculatorError


def run():
    calc = Calculator()
    # add the observers, one just prints stuff and the other autosaves
    calc.add_observer(LoggingObserver())
    calc.add_observer(AutoSaveObserver(calc))

    calc.load_history()  # load whatever was saved last time

    print("Calculator REPL. Type 'help' for commands.")

    while True:
        user_input = input(">>> ")
        user_input = user_input.strip()

        if user_input == "":
            continue

        if user_input == "exit":
            print("bye")
            break

        elif user_input == "help":
            print("commands: add, subtract, multiply, divide, power, root, history, undo, redo, save, load, clear, exit")

        elif user_input == "history":
            print(calc.get_history())

        elif user_input == "undo":
            res = calc.undo()
            if res is None:
                print("nothing to undo")
            else:
                print("undone")

        elif user_input == "redo":
            res = calc.redo()
            if res is None:
                print("nothing to redo")
            else:
                print("redone")

        elif user_input == "save":
            calc.save_history()
            print("saved")

        elif user_input == "load":
            calc.load_history()
            print("loaded")

        elif user_input == "clear":
            calc.clear_history()
            print("history cleared")

        else:
            # if it wasnt one of the keywords above, assume its a calculation
            # format should be like: add 3 5
            parts = user_input.split()

            if len(parts) != 3:
                print("invalid input, needs to be like: add 3 5")
                continue

            op = parts[0]
            num1 = parts[1]
            num2 = parts[2]

            try:
                result = calc.calculate(op, num1, num2)
                print("result:", result)
            except CalculatorError as e:
                print("error:", e)


if __name__ == "__main__":
    run()  # pragma: no cover