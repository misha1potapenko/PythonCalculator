import operations as op
import calculatortype as ty
import Komplex_Numbers

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

# operands = Insert_Numbers() # Это в ветку main, для запроса от пользователя двух комплексных чисел и какую операцию он хочет
# Строчки ниже тоже в main, здесь все вызовы функций. В зависимости от того, что пользователь хочет делать с двумя комплексными числами вызываются соответсвующие функции
# if operands[2] == "+":
#     record_in_file(Addition(Take_Rational_Part(operands[0]), Take_Symbol(operands[0]), Take_Imaginary_Part(operands[0]), Take_Rational_Part(operands[1]), Take_Symbol(operands[1]), Take_Imaginary_Part(operands[1])))
# elif operands[2] == "-":
#     record_in_file(Deduction(Take_Rational_Part(operands[0]), Take_Symbol(operands[0]), Take_Imaginary_Part(operands[0]), Take_Rational_Part(operands[1]), Take_Symbol(operands[1]), Take_Imaginary_Part(operands[1])))
# elif operands[2] == "*":
#     record_in_file(Multiply(Take_Rational_Part(operands[0]), Take_Symbol(operands[0]), Take_Imaginary_Part(operands[0]), Take_Rational_Part(operands[1]), Take_Symbol(operands[1]), Take_Imaginary_Part(operands[1])))
# else:
#     record_in_file(division(Take_Rational_Part(operands[0]), Take_Symbol(operands[0]), Take_Imaginary_Part(operands[0]), Take_Rational_Part(operands[1]), Take_Symbol(operands[1]), Take_Imaginary_Part(operands[1])))
