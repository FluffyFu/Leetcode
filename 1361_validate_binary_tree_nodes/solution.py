from queue import Queue


def valid(n, leftChild, rightChild):
    nodes = {i for i in range(len(leftChild))}
    in_degree = [0] * len(leftChild)

    for lc, rc in zip(leftChild, rightChild):
        if lc != -1:
            in_degree[lc] += 1
            if in_degree[lc] > 1:
                return False
            nodes.remove(lc)
        if rc != -1:
            in_degree[rc] += 1
            if in_degree[rc] > 1:
                return False
            nodes.remove(rc)

    if len(nodes) != 1:
        return False

    root = nodes.pop()
    q = Queue()
    q.put(root)

    seen = set()
    seen.add(root)

    while not q.empty():
        cur = q.get()

        if leftChild[cur] != -1:
            q.put(leftChild[cur])
            seen.add(leftChild[cur])
        if rightChild[cur] != -1:
            q.put(rightChild[cur])
            seen.add(rightChild[cur])

    return len(seen) == n

