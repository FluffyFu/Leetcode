
# dummy class
class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        return 1

    def dimensions(self) -> list:
        return []


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n_row, n_col = binaryMatrix.dimensions()
        j = n_col - 1
        found = False
        for i in range(n_row):
            if binaryMatrix.get(i, j) == 1:
                found = True
                while j > 0 and binaryMatrix.get(i, j-1) == 1:
                    j -= 1
                break
        while i < n_row-1:
            while j > 0 and binaryMatrix.get(i+1, j-1) == 1:
                j -= 1
            i += 1
        return j if found else -1

    def left_most_column_with_one_clean(self, binaryMatrix):
        n_row, n_col = binaryMatrix.dimensions()
        res = -1

        j = n_col - 1
        i = 0

        while i < n_row and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                res = j
                j -= 1
            else:
                i += 1

        return res


"""
0 0 0 1
0 0 1 1
0 1 1 1

n_row = 3, n_col = 4, j = 3

i = 0, j = 2, i = 1

"""

