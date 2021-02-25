def num_similar_group(strs):
    if not strs:
        return 0
    cnt = 0
    strs = set(strs)
    while len(strs) > 0:
        cur = strs.pop()
        dfs(cur, strs)
        cnt += 1

    return cnt


def dfs1(cur, strs):
    """
    O(N * k**2)  where k is the len of the string.
    """
    for i in range(len(cur)-1):
        for j in range(i+1, len(cur)):
            v = cur[:i] + cur[j] + cur[i+1:j] + cur[i] + cur[j+1:]
            if v in strs:
                strs.remove(v)
                dfs(v, strs)


def dfs(cur, strs):
    """
    O(N**2)
    """
    for v in neighbors(cur, strs):
        # check if v has already been removed.
        if v in strs:
            strs.remove(v)
            dfs(v, strs)


def neighbors(cur, strs):
    res = []
    for v in strs:
        cnt = 0
        for i in range(len(v)):
            if cur[i] != v[i]:
                cnt += 1
            if cnt > 2:
                break
        if cnt == 2:
            res.append(v)
    return res

