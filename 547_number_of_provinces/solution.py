def num_provinces(isConnected):
    n = len(isConnected)
    visited = set()

    res = 0
    for i in range(n):
        if i not in visited:
            dfs(i, isConnected, visited)
            res += 1

    return res


def dfs(cur, isConnected, visited):
    visited.add(cur)

    for i, val in enumerate(isConnected[cur]):
        if i not in visited and val:
            dfs(i, isConnected, visited)
