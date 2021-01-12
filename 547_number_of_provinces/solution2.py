def bfs(isConnected):
    n = len(isConnected)
    visited = set()
    res = 0

    for i in range(n):
        if i not in visited:
            to_visit = [i]

            while to_visit:
                cur = to_visit.pop()

                temp = []
                for j, val in enumerate(isConnected[cur]):
                    if j not in visited and val:
                        visited.add(j)
                        temp.append(j)
                to_visit += temp
            res += 1

    return res

