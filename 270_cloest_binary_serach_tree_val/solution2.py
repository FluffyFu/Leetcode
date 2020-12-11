def closest_val(root, target):
    res = [root.val]
    dfs(root, res, target)
    return res[0]


def dfs(node, res, target):
    if not node:
        return
    if abs(node.val-target) < abs(res[0]-target):
        res[0] = node.val

    if target < node.val:
        dfs(node.left, res, target)
    elif target > node.val:
        dfs(node.right, res, target)
