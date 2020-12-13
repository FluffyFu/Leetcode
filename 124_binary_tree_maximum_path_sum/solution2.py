def max_path_sum(root):
    res = [-float('inf')]
    max_path(root, res)

    return res[0]


def max_path(node, res):
    if not node:
        return -float('inf')
    left_sum = max(max_path(node.left, res), 0)
    right_sum = max(max_path(node.right, res), 0)

    res[0] = max(res[0], node.val + left_sum + right_sum)

    return node.val + max(left_sum, right_sum)
