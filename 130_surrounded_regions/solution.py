from queue import Queue


def solve(board):
    if not board:
        return

    n_row, n_col = len(board), len(board[0])

    b_points = set()
    b_points |= {(0, j) for j in range(n_col)}
    b_points |= {(n_row-1, j) for j in range(n_col)}
    b_points |= {(i, 0) for i in range(n_row)}
    b_points |= {(i, n_col-1) for i in range(n_row)}

    for i, j in b_points:
        if board[i][j] == 'O':
            q = Queue()
            q.put((i, j))
            board[i][j] = '*'

            while not q.empty():
                ci, cj = q.get()
                for vi, vj in neighbor(ci, cj, n_row, n_col):
                    if board[vi][vj] == 'O':
                        q.put((vi, vj))
                        board[vi][vj] = '*'
    for i in range(n_row):
        for j in range(n_col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '*':
                board[i][j] = 'O'


def neighbor(i, j, n_row, n_col):
    res = []
    if i > 0:
        res.append((i-1, j))
    if i < n_row - 1:
        res.append((i+1, j))
    if j > 0:
        res.append((i, j-1))
    if j < n_col - 1:
        res.append((i, j+1))

    return res

