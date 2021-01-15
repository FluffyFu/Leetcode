def max_len(arr):
    res = [0]
    dfs(0, set(), arr, res)
    return res[0]


def dfs(index, path, arr, res):
    res[0] = max(res[0], len(path))

    if index == len(arr):
        return

    for i in range(index, len(arr)):
        if len(set(arr[i])) != len(arr[i]):
            continue
        if not set(arr[i]) & path:
            dfs(i+1, path | set(arr[i]), arr, res)


def max_len_dp(arr):
    res = [set()]
    for a in arr:
        if len(a) != len(set(a)):
            continue
        for c in res[:]:
            if not c & set(a):
                res.append(c | set(a))

    return max(len(c) for c in res)


def max_len_recursion(arr):
    return dfs_re(set(), 0, arr)


def dfs_re(used: set, index: int, arr):
    """
    Given letters already used and the available words
    in the arr (arr[index:]). Return the max len
    """
    if index == len(arr):
        return len(used)

    max_l = dfs_re(used, index+1, arr)

    w = arr[index]
    if len(w) == len(set(w)) and not (used & set(w)):
        max_l = max(max_l, dfs_re(used | set(w), index+1, arr))

    return max_l

