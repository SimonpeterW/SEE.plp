number1=input("Enter First number: ")
number2=input("Enter the second number: ")
operation=input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = float(number1) + float(number2)
elif operation == '-':
    result = float(number1) - float(number2)
elif operation == '*':
    result = float(number1) * float(number2)
elif operation == '/':
    if float(number2) != 0:
        result = float(number1) / float(number2)
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print("The result is:", result)
# assignment.py
# This code performs basic arithmetic operations based on user input.
# It prompts the user for two numbers and an operation, then calculates and prints the result.  
# It handles division by zero and invalid operations gracefully.
# The code is designed to be simple and user-friendly, allowing for basic calculations.
# The code can be extended to include more operations or error handling as needed.
