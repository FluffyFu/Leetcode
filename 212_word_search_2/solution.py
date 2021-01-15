def search(board, words):
    if not board:
        return []
    res = []
    for word in words:
        if helper(board, word):
            res.append(word)
    return res


def helper(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0, word, board):
                return True
    return False


def dfs(i, j, k, word, board):
    if k == len(word):
        return True
    if i < 0 or i == len(board) or j < 0 or j == len(board) or board[i][j] != word[k]:
        return False
    temp = board[i][j]
    board[i][j] = '*'
    res = (dfs(i-1, j, k+1, word, board) or dfs(i+1, j, k+1, word, board) or
           dfs(i, j-1, k+1, word, board) or dfs(i, j+1, k+1, word, board))
    board[i][j] = temp
    return res
