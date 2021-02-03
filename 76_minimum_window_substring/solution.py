from collections import Counter


def min_win(s, t):
    """
    Counter stores how many times each character we still need in t.
    It can be negative. We use the sign of count to determine if the current
    letter contributes to the result.
    """
    counter = Counter(t)
    need = len(t)
    slow, fast = 0, 0
    min_len = float('inf')
    res = ''

    while fast < len(s):
        if s[fast] in counter:
            # only when we still need that letter, we decrease need
            if counter[s[fast]] > 0:
                need -= 1
            counter[s[fast]] -= 1

        # while the criterion is satisfied, move slow until it fails
        while need == 0:
            if fast - slow + 1 < min_len:
                min_len = fast - slow + 1
                res = s[slow:fast+1]
            if s[slow] in counter:
                counter[s[slow]] += 1
                if counter[s[slow]] > 0:
                    need += 1
            slow += 1
        fast += 1
    return res

