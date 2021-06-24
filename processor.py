def create_matrix():
    r, c = map(int, input('Enter matrix size: ').split())
    print('Enter matrix:')
    m = [input().split() for i in range(r)]
    for s in range(len(m)):
        m[s] = [float(x) for x in m[s]]
    return r, c, m


def create_two_matrix():
    r1, c1 = map(int, input('Enter size of first matrix: ').split())
    print('Enter first matrix:')
    mtrx1 = [input().split() for _ in range(r1)]
    for s in range(len(mtrx1)):
        mtrx1[s] = [float(x) for x in mtrx1[s]]
    r2, c2 = map(int, input('Enter size of second matrix: ').split())
    print('Enter second matrix:')
    mtrx2 = [input().split() for _ in range(r2)]
    for s in range(len(mtrx2)):
        mtrx2[s] = [float(x) for x in mtrx2[s]]
    return r1, c1, mtrx1, r2, c2, mtrx2


def transpose_matrix(row, column, matrix):
    trans_matrix = []
    for i in range(column):
        tmp = []
        for k in range(row):
            tmp.append(matrix[k][i])
        trans_matrix.append(tmp)
    return trans_matrix


def det_matrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            matrix_copy = [r[:] for r in matrix]
            t = matrix_copy[0][i]
            matrix_copy.pop(0)
            for row in matrix_copy:
                row.pop(i)
            det += t * (-1) ** i * det_matrix(matrix_copy)
        return det


def cof_matrix(matrix):
    cof = []
    for i in range(len(matrix)):
        tmp = []
        for k in range(len(matrix)):
            matrix_copy = [r[:] for r in matrix]
            matrix_copy.pop(i)
            for row in matrix_copy:
                row.pop(k)
            det = det_matrix(matrix_copy)
            tmp.append(det * (-1) ** (i + k))
        cof.append(tmp)
    return cof


while True:
    choice = input('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n'
                   '4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice: ')
    if choice == '1':
        sum_matrix = []
        row1, column1, matrix1, row2, column2, matrix2 = create_two_matrix()
        if row1 == row2 and column1 == column2:
            print('The result is:')
            for m1, m2 in zip(matrix1, matrix2):
                tmp = []
                for el1, el2 in zip(m1, m2):
                    tmp.append(el1 + el2)
                sum_matrix.append(tmp)
            for r in sum_matrix:
                print(*r)
        else:
            print('The operation cannot be performed.')
    elif choice == '2':
        row, column, matrix = create_matrix()
        n = float(input('Enter constant: '))
        mul_matrix = [[matrix[i][k] * n for k in range(column)] for i in range(row)]
        print('The result is:')
        for r in mul_matrix:
            print(*r)
    elif choice == '3':
        mul_matrix = []
        row1, column1, matrix1, row2, column2, matrix2 = create_two_matrix()
        if column1 == row2:
            for i1 in range(row1):
                tmp = []
                for i2 in range(column2):
                    n = 0
                    for k in range(column1):
                        n += matrix1[i1][k] * matrix2[k][i2]
                    tmp.append(n)
                mul_matrix.append(tmp)
            for r in mul_matrix:
                print(*r)
        else:
            print('The operation cannot be performed.')
    elif choice == '4':
        choice = input('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ')
        row, column, matrix = create_matrix()
        if choice == '1':
            trans_matrix = transpose_matrix(row, column, matrix)
            for r in trans_matrix:
                print(*r)
        elif choice == '2':
            trans_matrix = []
            for i in range(column):
                tmp = []
                for k in range(row):
                    tmp.append(matrix[row - 1 - k][column - 1 - i])
                trans_matrix.append(tmp)
            print('The result is:')
            for r in trans_matrix:
                print(*r)
        elif choice == '3':
            list(map(lambda x: x.reverse(), matrix))
            for r in matrix:
                print(*r)
        elif choice == '4':
            matrix.reverse()
            for r in matrix:
                print(*r)
    elif choice == '5':
        row, column, matrix = create_matrix()
        print('The result is:')
        print(det_matrix(matrix))
    elif choice == '6':
        row, column, matrix = create_matrix()
        det = det_matrix(matrix)
        if det != 0:
            matrix = cof_matrix(transpose_matrix(row, column, matrix))
            inv_matrix = [[matrix[i][k] * (1 / det) for k in range(column)] for i in range(row)]
            print('The result is:')
            for r in inv_matrix:
                print(*r)
        else:
            print('This matrix doesn\'t have an inverse.')
    elif choice == '0':
        exit()
