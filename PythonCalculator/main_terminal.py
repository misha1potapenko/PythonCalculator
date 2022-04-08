import operations as op
import calculatortype as ty

loop = 1
while loop == 1:
    if ty.type() ==  'racional':
        x = op.x()
        y = op.y()
        oper = op.selectoperation()
        res = op.res()
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'The result of {x} {oper} {y} = {res}\n')
        print(f'The result of {x} {oper} {y} = {res}\n(already written to txt file)' )
        again = input('Do you want calculate another numbers? Yes/No: ').lower()
        if again == 'yes':
            continue
        else:
            break