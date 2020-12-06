def k_smallest(root, k):
    res = []
    kg = []
    dfs(root, res, kg)
    return res[0]


def dfs(node, res, kg):
    if not node:
        return
    dfs(node.left, res, kg)
    kg[0] -= 1
    if kg[0] == 0:
        res.append(node.val)
    dfs(node.right, res, kg)


def k_smallest_iterative(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

