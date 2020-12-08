def lca(root, p, q):
    return dfs(root, p, q)


def dfs(node, p, q):
    """
    Returns the LCA of p, q if node contains p, q. If it only contains one of them,
    return p or q. If node does not contain p or q, return None.
    """
    if not node:
        return None
    if node == p or node == q:
        return node

    left = dfs(node.left, p, q)
    right = dfs(node.right, p, q)

    if left and right:
        return node
    elif left:
        return left
    elif right:
        return right
    else:
        return None

