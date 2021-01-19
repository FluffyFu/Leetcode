def max_gold(grid):
    if not grid:
        return 0

    max_gold = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] != 0):
                res = []
                visited = {(i, j)}
                dfs(i, j, visited, [], grid, res)
                max_gold = max(max_gold, max(res))

    return max_gold


def dfs(i, j, visited, path, grid, res):
    if finished(i, j, visited, grid):
        res.append(sum(path) + grid[i][j])
        return
    for n_i, n_j in neighbor(i, j, grid):
        if (n_i, n_j) not in visited and grid[n_i][n_j] != 0:
            visited.add((n_i, n_j))
            dfs(n_i, n_j, visited, path+[grid[i][j]], grid, res)


def neighbor(i, j, grid):
    neighbor = []
    if i - 1 >= 0:
        neighbor.append((i-1, j))
    if i + 1 <= len(grid) - 1:
        neighbor.append((i+1, j))
    if j - 1 >= 0:
        neighbor.append((i, j-1))
    if j + 1 < len(grid[0]):
        neighbor.append((i, j+1))
    return neighbor


def finished(i, j, visited, grid):
    neighbors = neighbor(i, j, grid)
    for i, j in neighbors:
        if (i, j) not in visited and grid[i][j] != 0:
            return False
    return True
