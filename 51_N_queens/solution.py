def solve(n):
    board = [['.'] * n for _ in range(n)]
    res = []
    dfs(0, board, res)
    return res


def dfs(i, board, res):
    if i == len(board):
        res.append(convert_res(board))
        return
    for j in range(len(board[i])):
        if is_valid(i, j, board):
            board[i][j] = 'Q'
            dfs(i+1, board, res)
            board[i][j] = '.'


def is_valid(cur_i, cur_j, board):
    n_col = len(board)
    for i in range(cur_i):
        if board[i][cur_j] == 'Q':
            return False
    d = max(cur_i - cur_j, cur_j - cur_i)

    for i in range(cur_i):
        j = i - (cur_i - cur_j)
        if j >= 0 and j < n_col and board[i][j] == 'Q':
            return False
        j = cur_i + cur_j - i
        if j >= 0 and j < n_col and board[i][j] == 'Q':
            return False

    return True


def convert_res(board):
    res = []
    for row in board:
        sub_res = []
        for e in row:
            if e == '#':
                sub_res.append('.')
            else:
                sub_res.append(e)
        res.append(''.join(sub_res))
    return res

