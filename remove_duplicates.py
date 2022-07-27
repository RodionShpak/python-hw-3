# ### Завдання 3
# Файл: `remove_duplicates.py`
# Оцінка: 25
# Створіть функцію `def remove_duplicates(array)` яка приймає цілочисельний масив, відсортований у порядку зростання, видаліть дублікати чисел, щоб кожен унікальний елемент з’являвся лише один раз. Функція має повертати новий масив без дуплікатів чисел, відносний порядок елементів має бути незмінним
# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі `remove_duplicates.py` повина бути створена функція `def remove_duplicates(array)` яка виконує необхідну логіку.
# Приклади:
# - `remove_duplicates([1,1,2])` -> [1,2]
# - `remove_duplicates([0,0,1,1,1,2,2,3,3,4])` -> [0,1,2,3,4]
# - `remove_duplicates([1,1,1,1,1,1,1,1])` -> [1]


# ДЕКІЛЬКА ВАРІАНТІВ: 


# 1) Перебором і фіксацією першого входження до нового списку ігноруючи решту входженнь

array = [1,1,1,2,2,3,3,4]
def remove_duplicates(array):
    arrayNew = []
    for i in array:
        if i not in arrayNew:
            arrayNew.append(i)
    print(arrayNew)
remove_duplicates(array)


# 2) Через модуль collections.OrderedDict.fromkeys().

# from collections import OrderedDict
# array = [0,0,1,1,1,2,2,3,3,4]
# def remove_duplicates(array):
#     arrayNew = list(OrderedDict.fromkeys(array))
#     print(arrayNew)
# remove_duplicates(array)


# 3) За допомогою set().

# array = [0,0,1,1,1,2,2,3,3,4,5,5,6,7]
# def remove_duplicates(array):
#     arrayNew = list(set(array))
#     print(arrayNew)
# remove_duplicates(array)

# 4) За допомогою генератор списка + enumarate()

# array = [0,0,1,1,1,2,2,3,3,4,5,5,6,7]
# def remove_duplicates(array):
#     arrayNew = [i for n, i in enumerate(array) if i not in array[:n]]
#     print(arrayNew)
# remove_duplicates(array)