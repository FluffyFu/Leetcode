def largest_bst(root):
    _, _, res = dfs(root)

    return res


def dfs(root):
    """
    Returns: min, max, largest_bst_size
    """
    if not root:
        return (float('inf'), -float('inf'), 0)

    left_res = dfs(root.left)
    right_res = dfs(root.right)

    # check if the current node is bst
    if root.val > left_res[1] and root.val < right_res[0]:
        return (min(left_res[0], root.val), max(right_res[1], root.val), left_res[2] + right_res[2] + 1)
    else:
        # use extreme value to label the bst no longer satisfied.
        return (-float('inf'), float('inf'), max(left_res[2], right_res[2]))


def dfs2(root):
    """
    Returns: min, max, largest_bst_size, valid_bst
    """
    if not root:
        return (float('inf'), -float('inf'), 0, True)
    left = dfs2(root.left)
    right = dfs2(root.right)

    if left[-1] and right[-1] and root.val > left[1] and root.val < right[0]:
        return (min(root.val, left[0]), max(root.val, right[1]), left[2] + right[2] + 1, True)
    else:
        return (None, None, max(left[2], right[2]), False)

