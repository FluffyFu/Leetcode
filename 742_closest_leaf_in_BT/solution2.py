from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_closest(root, k):
    graph = dict()
    cur = dfs(root, None, graph, k)
    if not cur.left and not cur.right:
        return cur.val

    q = deque()
    q.append((cur, 0))
    seen = set()

    while q:
        node, dist = q.popleft()

        for v in (node.left, node.right, graph.get(node, None)):
            if v and v not in seen:
                if not v.left and not v.right:
                    return v.val
                else:
                    q.append((v, dist+1))
                    seen.add(v)


def dfs(root, pre, graph, k):
    if not root:
        return None
    if root.val == k:
        graph[root] = pre
        return root
    graph[root] = pre
    left = dfs(root.left, root, graph, k)
    right = dfs(root.right, root, graph, k)

    return left if left else right

