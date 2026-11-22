num1= input('Enter first number: ')
num2 = input('Enter second number: ')
operator = input('Enter operator: ')

if operator == '+':
    print(f"{num1} {operator} {num2} = {int(num1) + int(num2)}")
elif operator == '-':
    print(f"{num1} {operator} {num2} = {int(num1) - int(num2)}")
elif operator == '*':
    print(f"{num1} {operator} {num2} = {int(num1) * int(num2)}")
elif operator == '/':
    print(f"{num1} {operator} {num2} = {int(num1) / int(num2)}")
