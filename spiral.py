# ### Завдання 4 (додаткове)

# Файл: `spiral.py`
# Оцінка: 25


# Створіть функцію `def spiral(matrix)` яка приймає цілочисельну матрицю розміром NxM та повертає масив в якому числа з матриці записані в порядку спіралі.
# Матриця виглядає наступним чином:
# ```
# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# ```
# Це масив цілочисельних масивів. 
# Наприклад матриця розміром 3x4 виглядає ось так:
# ```
# [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# ```
# Порядок спіралі виглядає ось так:  
# ![m1](https://raw.githubusercontent.com/vaiol/python/main/L3/src/m1.png)  
# ![m2](https://raw.githubusercontent.com/vaiol/python/main/L3/src/m2.png)

# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі `spiral.py` повина бути створена функція `def spiral(matrix)` яка виконує необхідну логіку.

# Приклади:
# - `spiral([[1,2,3],[4,5,6],[7,8,9]])` -> [1,2,3,6,9,8,7,4,5]
# - `spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])` -> [1,2,3,4,8,12,11,10,9,5,6,7]

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def spiral(matrix):
    matrixNew = []
    if len(matrix) == 0:
        return matrixNew
    rowBegin = 0
    rowEnd = len(matrix) - 1
    colBegin = 0
    colEnd = len(matrix[0]) - 1
    while rowBegin <= rowEnd and colBegin <= colEnd:
        for i in range(colBegin, colEnd + 1):
            matrixNew.append(matrix[rowBegin][i])
        rowBegin += 1
        for i in range(rowBegin, rowEnd+1):
            matrixNew.append(matrix[i][colEnd])
        colEnd -= 1
        if rowBegin <= rowEnd:
            for i in range(colEnd, colBegin-1, -1):
                matrixNew.append(matrix[rowEnd][i])
        rowEnd -= 1
        if colBegin <= colEnd:
            for i in range(rowEnd, rowBegin-1, -1):
                matrixNew.append(matrix[i][colBegin])
        colBegin += 1
    print(matrixNew)
spiral(matrix)