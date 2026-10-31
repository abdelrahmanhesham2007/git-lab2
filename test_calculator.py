"""A simple calculator supporting addition only."""


def calculate(a, b):
    """Calculate the sum of two numbers."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    return a + b


def main():
    print("Python Addition Calculator")
    print("Type 'exit' to quit.")

    while True:
        first = input("Enter first number: ").strip()

        if first.lower() == "exit":
            print("Goodbye!")
            break

        try:
            a = float(first)
            b = float(input("Enter second number: "))
            result = calculate(a, b)
            print("Result:", result)
        except (ValueError, TypeError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
