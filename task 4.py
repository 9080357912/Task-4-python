def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation! Please enter one of +, -, *, /.")

def calculator():
    print("Welcome to the simple calculator!")
    while True:
        num1 = get_number("Enter the first number: ")
        operation = get_operation()
        num2 = get_number("Enter the second number: ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"The result is: {result}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
