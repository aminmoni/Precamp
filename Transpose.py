def matrix_transpose(matrix:list):
    matrix_row = len(matrix)
    matrix_column = (lambda matrix=matrix: len(matrix[0]) if matrix_row > 0 else 0)()
    trans_matrix = [[0 for x in range(matrix_row)] for y in range(matrix_column)]

    for i in range(matrix_row):
        for j in range(matrix_column):
            trans_matrix[j][i] += matrix[i][j]

    return print(trans_matrix)

a = [[2, 3, 5], [6, 7, 8]]
matrix_transpose(a)
