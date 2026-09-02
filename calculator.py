import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    # Use CLI args if given (CI runs), else fall back to demo values
    if len(sys.argv) >= 3:
        a, b = float(sys.argv[1]), float(sys.argv[2])
    else:
        a, b = 10, 5

    print(f"Calculator run with a={a}, b={b}")
    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division: {a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()