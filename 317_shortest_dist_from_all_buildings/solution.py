from queue import Queue


def shortest(grid):
    if not grid or not grid[0]:
        return -1
    n_b = 0
    n_row = len(grid)
    n_col = len(grid[0])

    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == 1:
                n_b += 1

    res = int(10**6)

    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == 0:
                cum_sum = 0
                n_rb = 0

                visited = {(i, j)}
                q = Queue()
                q.put((i, j))
                dist = 0

                while not q.empty():
                    level_n = q.qsize()
                    dist += 1
                    for _ in range(level_n):
                        cur_i, cur_j = q.get()
                        for v_i, v_j in neighbors(cur_i, cur_j, n_row, n_col):
                            if (v_i, v_j) in visited:
                                continue
                            elif grid[v_i][v_j] == 1:
                                visited.add((v_i, v_j))
                                cum_sum += dist
                                n_rb += 1
                            elif grid[v_i][v_j] == 0:
                                visited.add((v_i, v_j))
                                q.put((v_i, v_j))
                if n_rb == n_b:
                    res = min(res, cum_sum)
    if res != int(10**6):
        return res
    return -1


def shortest_2(grid):
    """
    Two improvements: 1. start from 1 instead of 0, because if there is no feasible
    solution, it would terminate at the first BFS. 2. Append distance from the origin info,
    which simplifies the BFS loop.
    """
    n_row, n_col = len(grid), len(grid[0])
    n_b = sum(grid[i][j] == 1 for i in range(n_row) for j in range(n_col))
    dist = [[0] * n_col for _ in range(n_row)]
    hit = [[0] * n_col for _ in range(n_row)]

    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] != 1:
                continue
            visited = {(i, j)}
            q = Queue()
            q.put((i, j, 0))
            cnt1 = 1

            while not q.empty():
                cur_i, cur_j, d = q.get()
                for v_i, v_j in neighbors(cur_i, cur_j, n_row, n_col):
                    if (v_i, v_j) in visited:
                        continue
                    elif grid[v_i][v_j] == 0:
                        hit[v_i][v_j] += 1
                        dist[v_i][v_j] += (d + 1)
                        q.put((v_i, v_j, d + 1))
                    elif grid[v_i][v_j] == 1:
                        cnt1 += 1
                    visited.add((v_i, v_j))
            if cnt1 < n_b:
                return -1

    res = float('inf')
    for i in range(n_row):
        for j in range(n_col):
            if hit[i][j] == n_b:
                res = min(res, dist[i][j])
    # [[1, 1]], [[1]], [[1], [1]], these edge cases
    # won't trigger the return -1 in BFS
    return -1 if res == float('inf') else res


def neighbors(i, j, n_row, n_col):
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
