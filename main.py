
def calculator(first_number: int, second_number: int, operation: str) -> float | str:
    """A simple calculator that performs basic arithmetic operations."""

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            return"Error: Division by zero"
    else:
        return "Error: Invalid operation"

    return result

if __name__ == "__main__":
    first_number = 0
    second_number = 0
    operation = ''

    while True:
        try:
            first_number_str = input("Enter the first number: ")
            first_number = int(first_number_str)

            second_number_str = input("Enter the second number: ")
            second_number = int(second_number_str)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

    result = calculator(first_number, second_number, operation)
    print(f"The result of {first_number} {operation} {second_number} is: {result}")



