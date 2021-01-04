from collections import Counter


def find_permutation(s1, s2):
    c = Counter(s1)

    l, h = 0, 0

    while h < len(s2):
        if s2[h] in c and c[s2[h]] > 0:
            c[s2[h]] -= 1
            h += 1
        elif s2[h] in c and c[s2[h]] == 0:
            while s2[l] != s2[h]:
                if s2[l] in c:
                    c[s2[l]] += 1
                l += 1
            h += 1
            l += 1
        elif s2[h] not in c:
            c = Counter(s1)
            h += 1
            l = h

        if is_valid(c):
            return True

    return False


def is_valid(counter):
    for val in counter.values():
        if val != 0:
            return False
    return True


def find_permutation_clean(s1, s2):
    a = [ord(c) - ord('a') for c in s1]
    b = [ord(c) - ord('a') for c in s2]

    target = [0] * 26
    for c in a:
        target[c] += 1

    window = [0] * 26

    for i, c in enumerate(b):
        window[c] += 1

        if i >= len(s1):
            window[b[i - len(s1)]] -= 1

        if window == target:
            return True

    return False

