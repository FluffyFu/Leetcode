def find_longest(s):
    index = dict()
    l, r = 0, 0
    res = 0

    while r < len(s):
        if s[r] not in index:
            index[s[r]] = r
        else:
            index[s[r]] = r

        if len(index) > 2:
            min_cnt = len(s)
            min_c = None
            for c, cnt in index.items():
                if cnt < min_cnt:
                    min_cnt = cnt
                    min_c = c
            index.pop(min_c)
            l = min_cnt + 1

        res = max(res, r - l + 1)

        r += 1

    return res

