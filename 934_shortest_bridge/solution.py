from queue import Queue


def shortest_bridge(A):
    if not A:
        return None
    n_row, n_col = len(A), len(A[0])

    i, j = find_first(A)

    q = Queue()
    q.put((i, j))
    A[i][j] = -1

    bound = set()
    while not q.empty():
        cur = q.get()
        for v in find_neighbor(cur[0], cur[1], n_row, n_col):
            if A[v[0]][v[1]] == 1:
                q.put(v)
                A[v[0]][v[1]] = -1
            if A[v[0]][v[1]] == 0:
                bound.add((v))

    d = 1
    while len(bound) > 0:
        new = set()
        n_element = len(bound)
        for _ in range(n_element):
            cur = bound.pop()
            for v in find_neighbor(cur[0], cur[1], n_row, n_col):
                if A[v[0]][v[1]] == 1:
                    return d
                elif A[v[0]][v[1]] == 0:
                    A[v[0]][v[1]] = -1
                    new.add(v)
        d += 1
        bound = new


def find_first(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 1:
                return (i, j)


def find_neighbor(i, j, n_row, n_col):
    res = []
    if i < n_row - 1:
        res.append((i+1, j))
    if i > 0:
        res.append((i-1, j))
    if j > 0:
        res.append((i, j-1))
    if j < n_col - 1:
        res.append((i, j+1))

    return res
