array = [1,1,1,2,2,3,3,4]
def remove_duplicates(array):
    arrayNew = []
    for i in array:
        if i not in arrayNew:
            arrayNew.append(i)
    print(arrayNew)
remove_duplicates(array)