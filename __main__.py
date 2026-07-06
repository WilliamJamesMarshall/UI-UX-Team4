try:
    from . import add, division, minus, multiplication
except ImportError:
    from __init__ import add, division, minus, multiplication


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    first = get_number("First number: ")
    second = get_number("Second number: ")

    print(f"add: {add(first, second)}")
    print(f"minus: {minus(first, second)}")
    print(f"multiplication: {multiplication(first, second)}")
    print(f"division: {division(first, second)}")


if __name__ == "__main__":
    main()
