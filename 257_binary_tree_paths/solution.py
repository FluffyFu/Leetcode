def bt_path(root):
    res = []
    path = []
    dfs(root, res, path)

    return ["->".join(path) for path in res]


def dfs(node, res, path):
    if not node:
        return
    if not node.left and not node.right:
        res.append(list(path + [str(node.val)]))
        return

    dfs(node.left, res, path + [str(node.val)])
    dfs(node.right, res, path + [str(node.val)])

