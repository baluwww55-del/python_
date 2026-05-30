# SIMPLE CALCULATOR
# MENU DRIVEN PROGRAM

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def display_menu():
    print("\n### SIMPLE CALCULATOR ###")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    if choice in (1, 2, 3, 4):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == 2:
            print(f"{a} - {b} = {subtract(a, b)}")
        elif choice == 3:
            print(f"{a} * {b} = {multiply(a, b)}")
        elif choice == 4:
            print(f"{a} / {b} = {divide(a, b)}")
    else:
        print("Invalid choice. Please try again.")
# this is a simple calculator program that performs basic arithmetic operations like addition, subtraction, multiplication, and division based on user input.