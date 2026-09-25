print(" Calculator")


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


while True:

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    elif operator == "/":

        if num2 == 0:
            print("❌ Cannot divide by zero!")
            continue

        result = divide(num1, num2)

    else:
        print("❌ Invalid operator!")
        continue

    print("Result:", result)

    again = input("Do you want to calculate again? (y/n): ")

    if again.lower() != "y":
        print("Calculator closed.")
        break