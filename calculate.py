# ### Завдання 1

# Файл: `calculate.py`
# Оцінка: 50

# Покращити програму `calculate` (файл [calculate_raw.py](https://github.com/vaiol/python/blob/main/L3/src/calculate_raw.py)) яка була створена на лекції функцією виконання арифметичної операції в одній строчці. А також розширена новими арифметичними операціями.  
# Можна використовувати вихідний код вашої програми виконання відповідного ДЗ, але попередньо повинні бути виправлені помилки.  
# Програма має задовольняти наступні потреби:  
# 1. Створити файл `calculate.py` 
# 1. Программа повина зчитувати аргументи командної строки (за допомогою модуля `sys`) і виконувати арифметичні операції.
# 1. Необхідна підтримка 5 базових арифметичних операцій: `+`, `-`, `*`, `/`, `%` (додавання, віднімання, множення, ділення, остача від ділення). Додано нову операцію - %.
# 1. Результат виконання арифметичної операції потрібно виводити у консоль.
# 1. Программа повинна адекватно оброблювати помилки.
# 1. Программа повинна запускатись наступним чином: `python calculate.py 2 + 2` або `python calculate.py 2+2`
# 1. Приклади:
#     1. `python calculate.py 2 + 2` -> 4
#     1. `python calculate.py 2 - 200` -> -198
#     1.  `python calculate.py 2 * 8` -> 16
#     1.  `python calculate.py 200 / 2` -> 100 
#     1. `python calculate.py 3+3` -> 6
#     1. `python calculate.py 100-20` -> 80
#     1.  `python calculate.py 4*4` -> 16
#     1.  `python calculate.py 25/2` -> 12.5 
# 1. Заборонено використовувати `eval` для обчислення результату.
# 1. Повинна бути створена і використана функція обчислення `def calc(left_operand, right_operand, operation)` яка повертає результат арифметичного обчислення.



import sys
operation = []
allowed_operations = ['+', '-', '/', '*', '%', '//' ] # Додав ще цілочисельне ділення
if len(sys.argv) == 2:                        # щоб працював варіант "python calculate.py 2+2", в якому лівий операнд,оператор і правий операнд становлять один аргумент, потрібно відсортувати і розділити методом split
        for a in allowed_operations:
            separator = sys.argv[1].split(a)
            if len(separator) == 2:
                operation = a
                left_operand = separator[0]
                right_operand = separator[1]
                break
elif len(sys.argv) == 4:   # для варіанту python calculate.py 2 + 2, де 4 аргументи, по суті 3=)
	    left_operand = sys.argv[1]
	    right_operand = sys.argv[3]
	    operation = sys.argv[2]
def calc(left_operand, right_operand, operation):
    left_operand = int(left_operand)
    right_operand = int(right_operand)
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
    elif operation == '%':
        remainder_from_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand / right_operand)
        sys.exit()
    elif operation == '//':
        integer_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand // right_operand)
        sys.exit()
calc(left_operand, right_operand, operation)

#Потребує вдосконалення, тому що програма видасть помилку, на етапі перетворення їх в integer (45 рядок), якщо ми будемо використовувати данні які не трансформуються в число, наприклад літери.  




