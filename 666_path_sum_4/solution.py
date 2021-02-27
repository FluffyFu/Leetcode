def path_sum(nums):
    if not nums:
        return 0
    tree = create_map(nums)
    res = [0]

    dfs((1, 1), tree, 0, res)

    return res[0]


def create_map(nums):
    res = dict()

    for n in nums:
        r, c, v = list(str(n))
        res[(int(r), int(c))] = int(v)

    return res


def dfs(root, tree, pre_sum, res):
    if root not in tree:
        return
    if (root[0] + 1, 2 * root[1] - 1) not in tree and (root[0] + 1, 2 * root[1]) not in tree:
        res[0] += (pre_sum + tree[root])
        return

    dfs((root[0]+1, 2 * root[1] - 1), tree, pre_sum + tree[root], res)
    dfs((root[0]+1, 2 * root[1]), tree, pre_sum + tree[root], res)

