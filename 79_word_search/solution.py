def search(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(i, j, board, 1, word, {(i, j)}):
                return True
    return False


def dfs(i, j, board, k, word, visited):
    if k == len(word):
        return True

    for vi, vj in neighbor(i, j, len(board), len(board[0])):
        if (vi, vj) not in visited and board[vi][vj] == word[k]:
            visited.add((vi, vj))
            if dfs(vi, vj, board, k+1, word, visited):
                return True
            visited.remove((vi, vj))
    return False


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

