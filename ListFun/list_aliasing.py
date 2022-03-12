



# LIST ALIASING
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1 # list3 is an alias for the same list object that list1 refers
print(list1, list2, list3)
list3[1] = 200
print(list1, list2, list3)

# PYTHON IS PASS BY OBJECT REFERENCE
# object references are passed by value (copied)
# demo time!!
def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

def clear_out(table):
    table = []

matrix = [[1, 2, 3], [4, 5, 6]] # 2D list
print("matrix before:", matrix)
add_one(matrix) # the matrix object references is copied
# into the table parameter, thus making table an alias
print("matrix after:", matrix)

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix)

# SHALLOW VS DEEP COPIES
matrix_copy = matrix.copy() # shallow copy
# object references are copied, not the objects themselves
matrix_deep_copy = copy.deepcopy(matrix) # deep copy
# the objects are copied
print("matrix before:", matrix)
print("matrix_copy before:", matrix_copy)
print("matrix_deep_copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix_copy after:", matrix_copy)
print("matrix_deep_copy after:", matrix_deep_copy)
# you probably want a deep copy