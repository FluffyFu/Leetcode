from queue import Queue


def lca(root, p, q):
    ancestor = {root: None}
    que = Queue()
    que.put(root)

    while not que.empty():
        cur = que.get()
        if cur.left:
            que.put(cur.left)
            ancestor[cur.left] = cur
        if cur.right:
            que.put(cur.right)
            ancestor[cur.right] = cur

    p_ancestors = set()
    while p:
        p_ancestors.add(p)
        p = ancestor[p]

    while q:
        if q in p_ancestors:
            return q
        q = ancestor[q]

