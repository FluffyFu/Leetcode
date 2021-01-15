def exit(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, board, 0, word):
                return True
    return False


def dfs(i, j, board, k, word):
    if k == len(word):
        return True
    if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != word[k]:
        return False
    temp = board[i][j]
    board[i][j] = '*'
    res = (dfs(i-1, j, board, k+1, word) or dfs(i+1, j, board, k+1, word) or
           dfs(i, j-1, board, k+1, word) or dfs(i, j+1, board, k+1, word))
    board[i][j] = temp
    return res

