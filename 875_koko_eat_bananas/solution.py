import math


def min_speed(piles, H):
    r = max(piles)
    l = 1

    while l <= r:
        mid = l + (r-l) // 2
        total = 0
        for p in piles:
            total += math.ceil(p/mid)
        if total > H:
            l = mid + 1
        elif total == H:
            return mid
        else:
            r = mid - 1

    return l

