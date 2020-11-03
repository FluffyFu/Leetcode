class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def sum_region(self, row1, col1, row2, col2):
        res = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                res += self.matrix[i][j]

        return res


class NumMatrix2:
    """
    Assume the sum_region will be called multiple times. We can precalculate
    the accumulative sum of each row.
    """

    def __init__(self, matrix):
        self._matrix = matrix

        if not matrix:
            self._cum_matrix = [[0]]
        else:
            n_rows = len(matrix)
            n_cols = len(matrix[0])

            self._cum_matrix = [
                [0 for _ in range(n_cols)] for _ in range(n_rows)]
            for i in range(n_rows):
                cum_sum = 0
                for j in range(n_cols):
                    cum_sum += self._matrix[i][j]
                    self._cum_matrix[i][j] = cum_sum

    def sum_region(self, row1, col1, row2, col2):
        res = 0
        for i in range(row1, row2+1):
            res += (self._cum_matrix[i][col2] - self._cum_matrix[i][col1 - 1]
                    if col1-1 >= 0 else self._cum_matrix[i][col2])
        return res

