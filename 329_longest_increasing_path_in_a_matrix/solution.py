def longest_increase_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    nr, nc = len(matrix), len(matrix[0])
    dp = [[1 for _ in range(nc)] for _ in range(nr)]

    for i in range(nr):
        for j in range(nc):
            dp[i][j] = dfs(i, j, matrix, nr, nc, dp)

    return max(e for row in dp for e in row)


def dfs(i, j, matrix, nr, nc, dp):
    if dp[i][j] != 1 or not neighbors(i, j, nr, nc):
        return dp[i][j]

    dp[i][j] = max(dfs(v[0], v[1], matrix, nr, nc, dp) + 1 if matrix[i][j] < matrix[v[0]][v[1]] else 1
                   for v in neighbors(i, j, nr, nc))
    return dp[i][j]


def neighbors(i, j, nr, nc):
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

