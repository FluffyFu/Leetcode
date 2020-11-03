class NumMatrix:
    def __init__(self, matrix):
        if not matrix or len(matrix[0]) == 0:
            self._matrix = [[0]]
            self._cum_matrix = [[0]]
        else:
            self._matrix = matrix
            self._cum_matrix = [
                [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
            for i in range(len(matrix)):
                cum_sum = 0
                for j in range(len(matrix[0])):
                    cum_sum += self._matrix[i][j]
                    self._cum_matrix[i][j] = cum_sum

    def update(self, row, col, val):
        original_val = self._matrix[row][col]
        for j in range(col, len(self._matrix[0])):
            self._cum_matrix[row][j] = self._cum_matrix[row][j] - \
                original_val + val

        self._matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        res = 0
        for i in range(row1, row2+1):
            res += (self._cum_matrix[i][col2] - self._cum_matrix[i][col1-1]
                    if col1 - 1 >= 0 else self._cum_matrix[i][col2])
        return res

