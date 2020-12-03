from collections import Counter


def find_anagram(s, p):
    if not s or not p or len(p) > len(s):
        return None
    c = Counter(list(p))
    slow = 0
    res = []

    for fast in range(len(p)):
        if s[fast] in c:
            c[s[fast]] -= 1

    while fast < len(s):
        if is_valid(c):
            res.append(slow)

        if s[slow] in c:
            c[s[slow]] += 1
        slow += 1
        fast += 1
        if fast < len(s) and s[fast] in c:
            c[s[fast]] -= 1
    return res


def is_valid(c):
    for val in c.values():
        if val != 0:
            return False
    return True

