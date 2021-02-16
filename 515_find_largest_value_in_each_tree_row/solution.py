from collections import defaultdict


def largest_row_val(root):
    cache = defaultdict(list)
    dfs(root, 0, cache)
    res = []
    for i in range(len(cache)):
        res.append(max(cache[i]))
    return res


def dfs(root, row, cache):
    if not root:
        return
    cache[row].append(root.val)
    dfs(root.left, row+1, cache)
    dfs(root.right, row+1, cache)
