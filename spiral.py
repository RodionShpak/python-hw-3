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