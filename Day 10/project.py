from project_logo import logo

def clear():
    print("\n" * 100)

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return 

operations = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input('Enter the first number: '))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        if operation not in operations:
            print("Invalid operation. Please choose a valid operation.")
            continue

        num2 = float(input('Enter the second number: '))
        result = operations[operation](num1, num2)

        if result is None:  
            print("Error: Division by zero! Please try again.")
            continue

        print(f"{num1} {operation} {num2} = {result}")
        
        while True:

            choice = str(input("Type 'Y' to continue calculating with the result or 'N' to exit:")).strip().upper()
            if choice == 'Y':
                num1 = result
                break
            elif choice == 'N':
                should_continue = False
                clear()
                break
            else:
                print("Invalid input. You need to choose 'Y' or 'N'.")

calculator()
