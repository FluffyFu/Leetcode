def is_matrix(matrix):
    n_row, n_col = len(matrix), len(matrix[0])

    for d in range(-n_col + 2, n_row-1):
        for j in range(1, n_col):
            i = j + d
            if i > 0 and i < n_row and matrix[i][j] != matrix[i-1][j-1]:
                return False

    return True


def is_matrix_clean(matrix):
    n_row, n_col = len(matrix), len(matrix[0])

    for i in range(n_row-1):
        for j in range(n_col-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False

    return True

