import sys


def get_numbers():
    """Accept two numbers via command-line args (for CI) or input() (for manual runs)."""
    if len(sys.argv) >= 3:
        return float(sys.argv[1]), float(sys.argv[2])
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def main():
    a, b = get_numbers()
    print(f"Sum of {a} and {b} = {a + b}")


if __name__ == "__main__":
    main()