def partition(s):
    if not s:
        return []
    res = []
    path = []
    dfs(s, path, res)

    return res


def dfs(s, path, res):
    if s == '':
        res.append(path[:])
    for i in range(len(s)):
        if is_parlidrome(s[:i+1]):
            path.append(s[:i+1])
            dfs(s[i+1:], path, res)
            path.pop()


def is_parlidrome(s):
    l, h = 0, len(s) - 1
    while l < h:
        if s[l] == s[h]:
            l += 1
            h -= 1
        else:
            return False
    return True

