def larger(grid):
    if not grid or not grid[0]:
        return 0
    # label lands from 2
    label = 2
    land_size = dict()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                land_size[label] = dfs_without_cnt(i, j, label, grid)
                label += 1

    land_size[0] = 0

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                labels = set(grid[vi][vj] for vi, vj in move(i, j, grid))
                sub_res = sum(land_size[l] for l in labels) + 1
                res = max(res, sub_res)

    return res if res != 0 else len(grid) * len(grid[0])


def dfs(i, j, label, grid, cnt):
    grid[i][j] = label
    cnt[0] += 1
    for vi, vj in move(i, j, grid):
        if grid[vi][vj] == 1:
            dfs(vi, vj, label, grid, cnt)


def dfs_without_cnt(i, j, label, grid):
    res = 0
    grid[i][j] = label
    for vi, vj in move(i, j, grid):
        if grid[vi][vj] == 1:
            res += dfs_without_cnt(vi, vj, label, grid)
    return res + 1


def move(i, j, grid):
    for s, t in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= i + s < len(grid) and 0 <= j + t < len(grid[0]):
            yield i + s, j + t
