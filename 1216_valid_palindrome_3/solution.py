def is_valid(s, k):
    if not s:
        return True
    return back_track(s, k)


def back_track(s, k):
    """
    TLE
    """
    if k < 0:
        return False
    if is_palindrom(s):
        return True

    for i in range(len(s)):
        if back_track(s[:i] + s[i+1:], k-1):
            return True

    return False


def is_palindrom(s):
    if not s:
        return True
    l, h = 0, len(s) - 1

    while l < h:
        if s[l] != s[h]:
            return False
        l += 1
        h -= 1
    return True

