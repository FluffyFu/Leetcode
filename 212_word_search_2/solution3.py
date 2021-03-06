
def find_words(board, words):
    trie = dict()

    for w in words:
        temp_dict = trie
        for c in w:
            temp_dict = temp_dict.setdefault(c, dict())
        temp_dict['#'] = True

    nr, nc = len(board), len(board[0])

    res = set()
    for i in range(nr):
        for j in range(nc):
            if board[i][j] not in trie:
                continue
            seen = {(i, j)}
            path = [board[i][j]]
            dfs(i, j, board, trie[board[i][j]], res, path, seen, nr, nc)
    return list(res)


def dfs(i, j, board, trie, res, path, seen, nr, nc):
    if '#' in trie:
        res.add(''.join(path))

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in dirs:
        ni, nj = i + di, j + dj

        if 0 <= ni < nr and 0 <= nj < nc and board[ni][nj] in trie and (ni, nj) not in seen:
            seen.add((ni, nj))
            dfs(ni, nj, board, trie[board[ni][nj]],
                res, path + [board[ni][nj]], seen, nr, nc)
            seen.remove((ni, nj))


class Board:

    def __init__(self, board, words):
        self.nr = len(board)
        self.nc = len(board[0])
        self.board = board

        self.trie = dict()
        self.dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for w in words:
            temp = self.trie

            for c in w:
                temp = temp.setdefault(c, dict())
            temp['#'] = True

    def find_words(self):
        res = []
        for i in range(self.nr):
            for j in range(self.nc):
                if self.board[i][j] not in self.trie:
                    continue
                self.dfs(i, j, self.trie, {(i, j)}, [self.board[i][j]], [])
        return res

    def dfs(self, i, j, node, seen, path, res):
        if '#' in node:
            res.append(''.join(path))
            # avoid duplicate results
            node.pop('#', None)

        for di, dj in self.dirs:
            ni, nj = i + di, j + dj

            if 0 <= ni < self.nr and 0 <= nj < self.nc and (ni, nj) not in seen and self.board[ni][nj] in node:
                seen.add((ni, nj))
                self.dfs(ni, nj, node[self.board[ni][nj]], seen,
                         path + [self.board[ni][nj]], res)
                seen.remove((ni, nj))

