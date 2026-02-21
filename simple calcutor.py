# Simple Calculator

# Get user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get user input for operation
operation = input("Choose operation (+, -, *, /): ")

# Perform the chosen operation
if operation == '+':
    result = num1 + num2

elif operation == '-':
    result = num1 - num2

elif operation == '*':
    result = num1 * num2

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

else:
    result = "Invalid operation!"

# Display the result
print("Result:", result)
