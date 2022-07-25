# import sys



# if len(sys.argv) != 4:
#     print('Arg len should be 4')
#     sys.exit()

# # +, -, /, *

# # ['L3/src/calculate.py', '2', '+', '2']
# # [лівий операнд] [ариф опер] [правий опера]

# # PEP-8
# left_operand = sys.argv[1]
# right_operand = sys.argv[3]

# operation = sys.argv[2]

# allowed_operations = ['+', '-', '/', '*']

# if operation not in allowed_operations:
#     print('Operation is not allowed')
#     sys.exit()
# try:
#     left_operand = int(left_operand)
#     right_operand = int(right_operand)
# except ValueError:
#     print('Left and Right operands must be int')
#     sys.exit()

# if operation == '/' and right_operand == 0:
#     print('Division by zero is not allowed')
#     sys.exit()


# print(eval(f'{left_operand}{operation}{right_operand}'))


# '100/1'.split('/') # operation = /, left, right = ['100', '1']
# '100+1'.split('+') # ['100', '1'] 





import sys
left_operand = sys.argv[1]
right_operand = sys.argv[3]
operation = sys.argv[2]
def calculate(left_operand, right_operand, operation):
    left_operand = int(left_operand)
    right_operand = int(right_operand)
    allowed_operations = ['+', '-', '/', '*', '//', '%' ]
    if len(sys.argv) != 4:
        print('Arg len should be 4')
        sys.exit()
    if operation not in allowed_operations:
        print('Operation is not allowed')
        sys.exit()
    if operation == '/' and right_operand == 0:
        print('Division by zero is not allowed')
        sys.exit()
    elif operation == '+':
        addition = '{} + {} = '.format(left_operand, right_operand)
        print(left_operand + right_operand)
        sys.exit()
    elif operation == '-':
        subtraction = '{} - {} = '.format(left_operand, right_operand)
        print(left_operand - right_operand)
        sys.exit()
    elif operation == '*':
        multiplication = '{} * {} = '.format(left_operand, right_operand)
        print(left_operand * right_operand)
        sys.exit()
    elif operation == '/':
        division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand / right_operand)
        sys.exit()
    elif operation == '//':
        remainder_from_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand / right_operand)
        sys.exit()
    elif operation == '%':
        integer_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand // right_operand)
        sys.exit()
calculate(left_operand, right_operand, operation)