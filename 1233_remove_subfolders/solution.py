def remove(folder):
    folder = sorted(folder, reverse=True)
    res = []

    while len(folder):
        cur = folder.pop()
        res.append(cur)
        while len(folder) and is_sub(cur, folder[-1]):
            folder.pop()
    return res


def is_sub(f1, f2):
    return len(f2) > len(f1) and f2[:len(f1)] == f1 and f2.count('/') > f1.count('/')
