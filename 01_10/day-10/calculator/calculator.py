from art import logo

print(logo)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


calc_dict = {'+': add, '-': subtract, '*': multiply, '/': divide}
cont = 'y'
answer = ''

while cont == 'y' or cont == 'n':
    if not answer:
        num1 = float(input("Enter the first number\n"))
    else:
        num1 = answer
    print('Which of the following operations do you want to perform:')
    for op in calc_dict:
        print(op)
    operator = input('Enter the operator here:\n')
    num2 = float(input("Enter the second number\n"))
    answer = calc_dict[operator](num1, num2)
    print(f'{num1} {operator} {num2} = {answer}')
    cont = input(f'Continue with {answer}? (y/n) OR enter \'e\' to exit!').lower()
    if cont == 'n':
        answer = ''
