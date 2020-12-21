from collections import Counter


def is_palindrome(s):
    cnt = Counter(s)
    n_odd = 0
    for val in cnt.values():
        if val % 2 == 1:
            n_odd += 1

        if n_odd > 1:
            return False

    return True

