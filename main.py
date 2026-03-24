# Task 3.1

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

operation = input("Enter operation (+,-,*,/): ").strip()

result = None

if operation =='+':
    result = num1 + num2
elif operation =='-':
    result = num1 - num2
elif operation =='*':
    result = num1 * num2
elif operation =='/':
    if num2 != 0:
        result = num1 / num2
    else:
        print('Division by zero')
else:
    print('Error: Operation not supported')

if result is not None:
    print(f'Result: {result}')

