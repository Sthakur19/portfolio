# Write a Python function that takes a 2D matrix as input and
# returns a new matrix that is obtained by
# flipping the original matrix horizontally.
# For example:

# Input matrix
matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
# Flipped matrix (horizontal flip)
# flipped_matrix = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]


def flipped_matrix(matrix):
    matrix_row = len(matrix)
    matrix_col = len(matrix[0])
    fliped_matrix = []
    for i in range(matrix_row):
        fliped_matrix_row = []
        for j in range(matrix_col):
            fliped_matrix_row.append(0)
        fliped_matrix.append(fliped_matrix_row)

    for i in range(matrix_row):
        for j in range(matrix_col):
            fliped_matrix[i][j] = matrix[i][matrix_col - j - 1]
    
    print(fliped_matrix)

flipped_matrix(matrix)