def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    print("Welcome to Unique Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

display_menu()

while True:
    choice = input("Enter operation choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye!")
        break
    elif choice in ('1', '2', '3', '4'):
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")

        if choice == '1':
            print("Result of addition:", add(num1, num2))
        elif choice == '2':
            print("Result of subtraction:", subtract(num1, num2))
        elif choice == '3':
            print("Result of multiplication:", multiply(num1, num2))
        elif choice == '4':
            print("Result of division:", divide(num1, num2))
    else:
        print("Invalid choice. Please choose again.")
