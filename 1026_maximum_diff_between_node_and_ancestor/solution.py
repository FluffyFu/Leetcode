from math import abs


def max_diff(root):
    if not root:
        return 0
    res = [0]
    dfs(root, res)

    return res[0]


def dfs(node, res):
    """
    Return the max and min element in the subtree and modify the max diff accordingly.
    """
    if not node.left and not node.right:
        return node.val, node.val

    if node.right:
        r_max, r_min = dfs(node.right, res)
    else:
        r_max, r_min = node.val, node.val
    if node.left:
        l_max, l_min = dfs(node.left, res)
    else:
        l_max, l_min = node.val, node.val

    cur = node.val
    r_c = max(abs(cur - r_max), abs(cur - r_min))
    l_c = max(abs(cur - l_max), abs(cur - l_min))

    res[0] = max([res[0], r_c, l_c])

    return max([r_max, l_max, cur]), min([r_min, l_min, cur])

