import operations_racional as op
import calculatortype as ty
import operations_complex as opCom


type = ty.type()

while type ==  'racional':
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
    
while type == 'complex':
    operands = opCom.Insert_Numbers()
    if operands[2] == "+":
        opCom.record_in_file(opCom.Addition(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
    elif operands[2] == "-":
        opCom.record_in_file(opCom.Deduction(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
    elif operands[2] == "*":
        opCom.record_in_file(opCom.Multiply(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))
    else:
        opCom.record_in_file(opCom.division(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]), opCom.Take_Imaginary_Part(operands[0]), opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]), opCom.Take_Imaginary_Part(operands[1])))