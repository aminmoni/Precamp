def determinant(mat1: list):
    mat1_row = len(mat1)
    mat1_col = (lambda matrix1=mat1: len(mat1[0]) if mat1_row>0 else 0)()

    if mat1_row == mat1_col:
        while len(mat1) >2:
            mat1_row1 = len(mat1)
            mat1_col1 = (lambda matrix1=mat1: len(mat1[0]) if mat1_row1 > 0 else 0)()

            result = [[0 for x in range(mat1_col1 - 1)] for y in range(mat1_row1 - 1)]

            for i in range(len(result)):
                for j in range(len(result)):
                      x = mat1[0][0]
                      y = mat1[i + 1][j + 1]
                      z = mat1[i + 1][0]
                      q = mat1[i][j + 1]
                      result[i][j] +=  x*y-z*q


            return print(result)
        else:
            return print('esle')
    else:
       return print('it is not square matrix')

a = [[4,2,-2, 5] , [10,6,2,6], [6,1,7,76],[144,66,3,2]]
determinant(a)
