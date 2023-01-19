import numpy
matrix = numpy.empty((3, 3))

# MATRIX 1
for i in range (0, 3):
    for j in range (0, 3):
        if(i == j):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
        print(f'{matrix[i][j]:.0f}', " ", end='')
    print("\n")
    
print("\n")
    
# MATRIX 2
for i in range (0, 3):
    for j in range (0, 3):
        if(i != j):
            matrix[i][j] += 3
        print(f'{matrix[i][j]:.0f}', " ", end='')
    print("\n")
        
print("\n")
        
# MATRIX 3
matrix = numpy.delete(matrix, (2), axis = 1)
for i in range(0, 3):
    for j in range (0, 2):
        print(f'{matrix[i][j]:.0f}', " ", end='')
    print("\n")
