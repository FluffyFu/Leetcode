from collections import Counter


def num(ages):
    """
    O(n**2) solution TLE.
    """
    res = 0
    for i in range(len(ages)):
        for j in range(len(ages)):
            if i != j:
                res += request(ages[i], ages[j])
    return res


def request(a, b):
    if (b <= 0.5 * a + 7) or (b > a) or (b > 100 and a < 100):
        return 0
    return 1


def num_fast(ages):
    """
    Even if a == b, they are not necessarily friends. for example a == 1.
    """
    counter = Counter(ages)
    res = 0
    for a in counter:
        for b in counter:
            if request(a, b):
                res += counter[a] * (counter[b] - (a == b))

    return res


def num_b(ages):
    """
    O(3 * Nlog(N))
    """
    ages = sorted(ages)
    res = 0
    for a in ages:
        low_t = int(0.5 * a + 8)
        low_i = low_b_inclusive(ages, low_t)
        up_i = up_b_inclusive(ages, a)

        # remove infeasible results
        res += max(0, up_i - low_i)
    return res


def low_b_inclusive(ages, target):
    """
    Returns the smallest index s.t. ages[i] >= target
    """
    left, right = 0, len(ages) - 1
    while left <= right:
        mid = (right + left)//2
        if ages[mid] >= target:
            right = mid - 1
        elif ages[mid] < target:
            left = mid + 1
    return left


def up_b_inclusive(ages, target):
    """
    Returns the largest index s.t. ages[i] <= target
    """
    l, r = 0, len(ages) - 1
    while l <= r:
        mid = (l + r) // 2
        if ages[mid] <= target:
            l = mid + 1
        elif ages[mid] > target:
            r = mid - 1
    return r


def norm_bs(ages, t):
    """
    Find t's index or return the index where t should be inserted (i.e.
    the index of the smallest number greater than t.)
    """
    left, right = 0, len(ages) - 1
    while left <= right:
        mid = (right + left) // 2
        if ages[mid] == t:
            return mid
        elif ages[mid] > t:
            right = mid - 1
        else:
            left = mid + 1
    return left

