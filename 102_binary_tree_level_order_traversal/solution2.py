from queue import Queue


def level_traversal(root):
    res = []
    if not root:
        return res
    level = [root]

    while level:
        new_level = []
        sub_res = []
        for node in level:
            sub_res.append(node.val)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        res.append(sub_res)

        level = new_level

    return res

