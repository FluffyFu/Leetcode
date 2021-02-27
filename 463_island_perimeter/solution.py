from collections import deque


def perimeter(grid):
    if not grid or not grid[0]:
        return 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    nr, nc = len(grid), len(grid[0])

    res = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 1:
                cnt = 4
                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < nr and 0 <= nj < nc and grid[ni][nj] == 1:
                        cnt -= 1
                res += cnt
    return res

