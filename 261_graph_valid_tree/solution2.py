def validate(n, edges):
    parent = dict()

    for x, y in edges:
        if find(x, parent) == find(y, parent):
            return False
        union(x, y, parent)

    if len(set([find(i, parent) for i in range(n)])) == 1:
        return True
    else:
        return False


def find(x, parent):
    parent.setdefault(x, x)
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent):
    parent[find(x, parent)] = find(y, parent)
