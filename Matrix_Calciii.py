def options():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def transpose_options():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (int(matrix[i][j]*100))/100
            print(f'{matrix[i][j]:10.2f}', end=' ')
        print()
    print()


def construct_matrix(number):
    row, col = list(map(int, input("Enter matrix size:").lstrip(' ').split(" ")))
    print(f"Enter{number} matrix:")
    matrix = []
    for i in range(row):
        entries = list(map(float, input().lstrip(' ').split(" ")))
        l = []
        for entry in entries:
            l.append(entry)
        matrix.append(l)

    return row, col, matrix


def transpose_side_diagonal(matrix):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[len(matrix) - 1 - j][len(matrix) - 1 - i]
    return result


def transpose_main_diagonal(matrix):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[j][i]
    return result


def transpose_vertically(matrix):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][len(matrix) - 1 - j]
    return result


def transpose_horizontally(row, col, matrix):
    result = [[0 for j in range(col)] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[len(matrix) - 1 - i][j]
    return result


def sum_matrix(row_A, col_A, row_B, col_B, matrix_A, matrix_B):
    if row_A != row_B or col_A != col_B:
        print('The operation cannot be performed.')
    else:
        result = [[0 for j in range(col_A)] for i in range(row_A)]
        for i in range(row_A):
            for m in range(len(matrix_A[0])):
                result[i][m] = round(float(matrix_A[i][m]) + float(matrix_B[i][m]),2)
        print_matrix(result)


def constant_multiply_matrix(matrix, constant):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][j] = constant * matrix[i][j]
    return result


def mul_matrix(row_A, col_A, row_B, col_B, matrix_A, matrix_B):
    if col_A == row_B:
        result = [[0 for j in range(col_B)] for i in range(row_A)]
        for i in range(row_A):
            for j in range(col_B):
                for k in range(col_A):
                    result[i][j] = result[i][j] + matrix_A[i][k] * matrix_B[k][j]
        print_matrix(result)
    else:
        print('Multiplying matrices is not possible')


def minor(row, col, matrix):
    return [mat[:col] + mat[col + 1:] for mat in (matrix[:row] + matrix[row + 1:])]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(len(matrix[0])):
            det += ((-1) ** j) * matrix[0][j] * determinant(minor(0, j, matrix))

    return det

def adjoint(matrix):
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    if len(matrix) == 1:
        result[0][0] = matrix[0][0]
    elif len(matrix) == 2:
        result[0][0] = matrix[1][1]
        result[0][1] = (-1) * matrix[1][0]
        result[1][0] = (-1) * matrix[0][1]
        result[1][1] = matrix[0][0]
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                min = minor(i, j, matrix)
                result[i][j] = ((-1) ** (i + j)) * determinant(min)
    return transpose_main_diagonal(result)



def inverse_matrix(matrix_A):
    if determinant(matrix_A) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        inv_det = (1 / determinant(matrix_A))
        inverse = constant_multiply_matrix(adjoint(matrix_A), inv_det)
        print('The result is:')
        return inverse


def choice(ch):
    if ch == 1:
        row_A, col_A, matrix_A = construct_matrix(' First')
        row_B, col_B, matrix_B = construct_matrix(' Second')
        print('The result is:')
        sum_matrix(row_A, col_A, row_B, col_B, matrix_A, matrix_B)
    elif ch == 2:
        row, col, matrix_A = construct_matrix('')
        constant = float(input("Enter constant:"))
        print('The result is:')
        print_matrix(constant_multiply_matrix(matrix_A, constant))
    elif ch == 3:
        row_A, col_A, matrix_A = construct_matrix(' First')
        row_B, col_B, matrix_B = construct_matrix(' Second')
        print('The result is:')
        mul_matrix(row_A, col_A, row_B, col_B, matrix_A, matrix_B)
    elif ch == 4:
        print()
        transpose_options()
        transpose_choice = int(input('Your choice:').lstrip(' '))
        if transpose_choice == 1:
            row, col, matrix_A = construct_matrix('')
            print_matrix(transpose_main_diagonal(matrix_A))
        elif transpose_choice == 2:
            row, col, matrix_A = construct_matrix('')
            print_matrix(transpose_side_diagonal(matrix_A))
        elif transpose_choice == 3:
            row, col, matrix_A = construct_matrix('')
            print_matrix(transpose_vertically(matrix_A))
        elif transpose_choice == 4:
            row, col, matrix_A = construct_matrix('')
            print_matrix(transpose_horizontally(row, col, matrix_A))
    elif ch == 5:
        row, col, matrix_A = construct_matrix('')
        print(determinant(matrix_A))
        print()
    elif ch == 6:
        row, col, matrix = construct_matrix('')
        if determinant(matrix) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print_matrix(inverse_matrix(matrix))
        print()


# main program
options()
ch = int(input("Your choice:").lstrip(' '))
while ch != 0:
    choice(ch)
    options()
    ch = int(input("Your choice:").lstrip(' '))
