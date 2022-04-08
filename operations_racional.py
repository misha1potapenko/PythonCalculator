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
