def range_sum(root, low, high):
    res = [0]
    dfs(root, low, high, res)
    return res[0]


def dfs(root, low, high, res):
    if not root or low > high:
        return
    if root.val < low:
        dfs(root.right, low, high, res)
    elif root.val > high:
        dfs(root.left, low, high, res)
    else:
        res[0] += root.val
        dfs(root.left, low, root.val-1, res)
        dfs(root.right, root.val+1, high, res)

