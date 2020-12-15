from collections import defaultdict


def group(strings):
    res = defaultdict(list)

    for s in strings:
        if not s:
            res[-1].append(s)
        sub_res = [0]
        for c in s[1:]:
            sub_res.append((ord(c) - ord(s[0])) % 26)

        sub_res = tuple(sub_res)
        res[sub_res].append(s)

    return [val for val in res.values()]

