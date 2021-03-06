from collections import defaultdict


def diag_sort(mat):
    if not mat or not mat[0]:
        return mat
    nr = len(mat)
    nc = len(mat[0])

    if nr == 1 or nc == 1:
        return mat

    data = defaultdict(list)

    for d in range(-(nc-1), nr):
        for i in range(nr):
            j = i - d
            if 0 <= j < nc:
                data[d].append(mat[i][j])

    for k in data.keys():
        data[k] = sorted(data[k], reverse=True)

    res = [[0] * nc for _ in range(nr)]

    for d in range(-(nc-1), nr):
        for i in range(nr):
            j = i - d
            if 0 <= j < nc:
                res[i][j] = data[d].pop()

    return res


def diag_sort_clean(mat):
    if not mat or not mat[0]:
        return mat
    nr = len(mat)
    nc = len(mat[0])

    if nr == 1 or nc == 1:
        return mat
    data = defaultdict(list)

    for i in range(nr):
        for j in range(nc):
            data[i-j].append(mat[i][j])

    for k in data.keys():
        data[k] = sorted(data[k], reverse=True)

    for i in range(nr):
        for j in range(nc):
            mat[i][j] = data[i-j].pop()

    return mat

