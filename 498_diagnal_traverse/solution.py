def diag(matrix):

    n_row, n_col = len(matrix), len(matrix[0])
    res = []

    for s in range(n_row + n_col - 1):
        if s % 2 == 0:
            row = min(s, n_row-1)
            col = s - row
            while row >= 0 and col < n_col:
                res.append(matrix[row][col])
                col += 1
                row -= 1
        elif s % 2 == 1:
            col = min(s, n_col-1)
            row = s - col
            while col >= 0 and row < n_row:
                res.append(matrix[row][col])
                col -= 1
                row += 1
    return res

