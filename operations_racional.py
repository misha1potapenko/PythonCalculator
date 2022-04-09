import operations_racional as op
import sys

def x():
    global firstnum
    firstnum = float(input('Choose first float number: '))
    return firstnum

def y():
    global secondnum
    secondnum = float(input('Choose second float number: '))
    return secondnum


def selectoperation():
    global operation
    operation = (input(f'Select operation: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res():
    if  operation == '+':
        res = firstnum + secondnum
        return res
    elif operation == '-':
        res = firstnum - secondnum
        return res
    elif operation == '*':
        res = firstnum * secondnum
        return res
    elif operation == '/':
        res = firstnum / secondnum
        return res
    else:
        print('invalid syntax')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res()
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'The result of {x} {oper} {y} = {res}\n')
        print(f'The result of {x} {oper} {y} = {res}\n(already written to txt file)' )
        again = input('Do you want calculate another numbers? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('Do you want to use the result of the last operation? (Yes/No): ').lower()
            if useresult == 'yes':
                x = res
                continue
            else:
                break              
        else:   
            sys.exit()