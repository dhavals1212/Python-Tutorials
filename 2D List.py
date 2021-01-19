matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#For a 3*3 matrix, the 2D list will be like the one shown above.
#In it, [1,2,3] show the first entity, hence their index is 0.

print(matrix[0][0])
#Here we have accessed the first number which is 1.
#To do that we called first row and first column.

for row in matrix:
    for item in row:
        print(item)