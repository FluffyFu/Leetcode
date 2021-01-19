def restore(s):
    res = []
    path = []
    dfs(0, 0, path, res, s)
    return res


def dfs(pre, k, path, res, s):
    if k == 3 and is_valid(s, pre, len(s)):
        res.append(create_ip(path, s))
        return
    for cur in range(pre+1, pre+4):
        if is_valid(s, pre, cur):
            dfs(cur, k+1, path + [cur], res, s)


def is_valid(s, start, end):
    if end > len(s) or start > len(s):
        return False
    if end - start > 3:
        return False
    if start == end:
        return False
    if end - start > 1 and s[start] == '0':
        return False
    n = int(s[start:end])
    return n >= 0 and n <= 255


def create_ip(path, s):
    start = [0] + path
    end = path + [len(s)]

    res = []
    for left, right in zip(start, end):
        res.append(s[left:right])

    return '.'.join(res)

