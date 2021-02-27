class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        flag = 1
        if player == 2:
            flag = -1

        self.rows[row] += flag
        self.cols[col] += flag

        if row == col:
            self.diag += flag
        if row + col == self.n-1:
            self.anti_diag += flag

        if self.rows[row] == self.n or self.cols[col] == self.n or self.diag == self.n or self.anti_diag == self.n:
            return 1

        if self.rows[row] == -self.n or self.cols[col] == -self.n or self.diag == -self.n or self.anti_diag == -self.n:
            return 2

        return 0

