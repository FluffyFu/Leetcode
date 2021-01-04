def find_longest(s, k):
    index = dict()
    l, r = 0, 0
    res = 0

    while r < len(s):
        if s[r] not in index:
            index[s[r]] = r
        else:
            index[s[r]] = r

        if len(index) > k:
            min_index = min(index.values())
            l = min_index + 1
            index.pop(s[min_index])
        res = max(res, r - l + 1)

        r += 1

    return res

