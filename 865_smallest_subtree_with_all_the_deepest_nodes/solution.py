def find_node(root):
    return depth_subtree(root)[1]


def depth_subtree(root):
    """
    Return the depth of the root and the subtree contains the deepest nodes.

    Returns:
        (int, Node)
    """
    if not root:
        return 0, None
    l = depth_subtree(root.left)
    r = depth_subtree(root.right)

    if l[0] > r[0]:
        return l[0] + 1, l[1]
    elif l[0] < r[0]:
        return r[0] + 1, r[1]
    else:
        return l[0] + 1, root

