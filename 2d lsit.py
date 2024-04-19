matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)
matrix.append([10,20,30])
matrix.remove([10,20,30])
matrix.insert(0,[10,20,30] )
#matrix.clear()
matrix.pop()
print([1,2,3] in matrix)
print(matrix)