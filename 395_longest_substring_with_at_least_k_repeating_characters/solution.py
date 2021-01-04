from collections import defaultdict


def find_longest(s, k):
    res = 0

    for h in range(1, 27):
        n_unique = 0
        eq_more_k = 0
        l, r = 0, 0

        counts = defaultdict(int)

        while r < len(s):
            if n_unique <= h:
                if s[r] not in counts or counts[s[r]] == 0:
                    n_unique += 1
                counts[s[r]] += 1

                if counts[s[r]] == k:
                    eq_more_k += 1

                r += 1

            elif n_unique > h:
                if counts[s[l]] == k:
                    eq_more_k -= 1
                counts[s[l]] -= 1

                if counts[s[l]] == 0:
                    n_unique -= 1
                l += 1

            if (n_unique == h) and (eq_more_k == h):
                res = max(res, r-l)

    return res

