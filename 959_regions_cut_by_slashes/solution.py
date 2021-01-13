def cut(grid):
    if not grid:
        return 0
    n_row, n_col = len(grid), len(grid[0])
    parent = dict()

    for i in range(n_row):
        for j in range(n_col):
            if i:
                union((i-1, j, 2), (i, j, 0), parent)
            if j:
                union((i, j-1, 1), (i, j, 3), parent)
            if grid[i][j] != '/':
                union((i, j, 0), (i, j, 1), parent)
                union((i, j, 3), (i, j, 2), parent)
            if grid[i][j] != '\\':
                union((i, j, 0), (i, j, 3), parent)
                union((i, j, 1), (i, j, 2), parent)

    res = set()
    for key in parent.keys():
        res.add(find(key, parent))

    return len(res)


def find(x, parent):
    """
    Find the parent of x and performs path compression
    """
    parent.setdefault(x, x)
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    parent[find(x, parent)] = find(y, parent)
