def candy(board):
    n_row, n_col = len(board), len(board[0])

    while True:
        crash = set()
        for i in range(n_row):
            for j in range(n_col):
                if i > 1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                    crash = crash | {(i, j), (i-1, j), (i-2, j)}

                if j > 1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                    crash = crash | {(i, j), (i, j-1), (i, j-2)}
        if not crash:
            break
        for i, j in crash:
            board[i][j] = 0

        for j in range(n_col):
            idx = n_row - 1

            for i in range(n_row-1, -1, -1):
                if board[i][j]:
                    board[idx][j] = board[i][j]
                    idx -= 1

            for i in range(idx+1):
                board[i][j] = 0

    return board

