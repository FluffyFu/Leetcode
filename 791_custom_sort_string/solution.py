from collections import Counter


def sort(S, T):
    c2s = {c: n for c, n in zip(S, range(len(S)))}

    val = len(S)
    for c in T:
        if c not in c2s:
            c2s[c] = val
            val += 1
    s2c = {n: c for c, n in c2s.items()}

    temp = [c2s[c] for c in T]
    temp = sorted(temp)
    res = [s2c[c] for c in temp]

    return ''.join(res)


def sort2(S, T):
    counter = Counter(T)
    res = []
    for c in S:
        if c in counter:
            res += [c] * counter[c]
            counter.pop(c)

    for c, v in counter.items():
        res += [c] * v

    return ''.join(res)

