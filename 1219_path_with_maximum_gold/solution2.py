def get_max(grid):
    if not grid:
        return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res = max(dfs(i, j, grid), res)

    return res


def dfs(i, j, grid):
    if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 0:
        return 0
    cur_val = grid[i][j]
    grid[i][j] = 0
    max_val = 0
    for n_i, n_j in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        max_val = max(dfs(n_i, n_j, grid), max_val)

    grid[i][j] = cur_val
    return max_val + cur_val

