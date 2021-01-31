def max_diff(root):
    res = [0]
    dfs(root, 0, 100000, res)
    return res[0]


def dfs(node, max_val, min_val, res):
    """
    Top-down approach. Keep track of the max and min encountered when going down.
    When reaching a leaf, the max diff is max_val - min_val. Since dfs covers all the
    path, the max diff path is included.
    """
    if not node:
        res[0] = max(res[0], max_val - min_val)
        return
    dfs(node.left, max(max_val, node.val), min(min_val, node.val), res)
    dfs(node.right, max(max_val, node.val), min(min_val, node.val), res)

