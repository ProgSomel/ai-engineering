#Simple Calculator
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

op = input("Enter operator: ")

if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid operator")