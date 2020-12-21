def longest_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    nr, nc = len(matrix), len(matrix[0])

    visited = dict()
    for i in range(nr):
        for j in range(nc):
            dfs(i, j, matrix, visited, nr, nc)

    return max(visited[(i, j)] for i in range(nr) for j in range(nc))


def dfs(i, j, matrix, visited, nr, nc):
    if (i, j) in visited:
        return visited[(i, j)]

    res = []
    for v in neighbor(i, j, nr, nc):
        if matrix[i][j] < matrix[v[0]][v[1]]:
            res.append(dfs(v[0], v[1], matrix, visited, nr, nc) + 1)
    if res:
        visited[(i, j)] = max(res)
    else:
        visited[(i, j)] = 1

    return visited[(i, j)]


def neighbor(i, j, nr, nc):
    res = []
    if i > 0:
        res.append((i-1, j))
    if i < nr - 1:
        res.append((i+1, j))
    if j > 0:
        res.append((i, j-1))
    if j < nc - 1:
        res.append((i, j+1))

    return res

