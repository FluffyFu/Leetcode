from collections import defaultdict


def group_strings(strings):
    group = defaultdict(list)
    for s in strings:
        key = cal_key(s)
        group[key].append(s)

    return [g for g in group.values()]


def cal_key(s):
    if len(s) == 1:
        return ()
    else:
        res = []
        for i in range(len(s) - 1):
            diff = ord(s[i]) - ord(s[i+1]) % 26
            res.append(diff)
    return tuple(res)

