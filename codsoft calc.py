import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def modulus(a, b):
    return a % b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def calculator():
    operations = {
        '1': ("Add", add),
        '2': ("Subtract", subtract),
        '3': ("Multiply", multiply),
        '4': ("Divide", divide),
        '5': ("Modulus", modulus),
        '6': ("Exponentiate", exponentiate),
        '7': ("Square Root", square_root),
        '8': ("Exit", None)
    }

    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("\nEnter the number of the operation you want to perform: ")

        if choice in operations:
            if choice == '8':
                print("Exiting the calculator. Goodbye!")
                break

            if choice == '7':
                try:
                    num = float(input("Enter the number: "))
                    print(f"Square root of {num} = {square_root(num)}")
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                continue

            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"{operation_name} of {num1} and {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
