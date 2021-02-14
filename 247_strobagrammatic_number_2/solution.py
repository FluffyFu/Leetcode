def find(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1', '8']
    path = []
    res = []
    backtrack(0, path, res, n)
    return sorted(res)


c_map = {'6': '9',
         '8': '8',
         '1': '1',
         '0': '0',
         '9': '6'}


def backtrack(i, path, res, n):
    if n % 2 == 0 and i == n // 2:
        res.append(half(path, n))
        return
    if n % 2 == 1 and i == n // 2 + 1:
        res.append(half(path, n))
        return
    if i == 0:
        for c in ('1', '6', '9', '8'):
            backtrack(i+1, path + [c], res, n)
    elif 0 < i < n // 2:
        for c in ('1', '6', '8', '9', '0'):
            backtrack(i+1, path + [c], res, n)
    elif n % 2 == 1 and i == n // 2:
        for c in ('1', '8', '0'):
            backtrack(i+1, path + [c], res, n)


def half(path, n):
    res = [None] * n
    k = n // 2 if n % 2 == 0 else (n+1) // 2
    for i in range(k):
        res[i] = path[i]
        res[n-1-i] = c_map[path[i]]

    return ''.join(res)
