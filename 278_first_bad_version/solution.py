
def find_bad_version(self, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1

    return low


"""
T, T, T, F, F

low = 0, high = 4, mid = 2
low = 3, hight = 4, mid = 3
low = 3, high = 3, mid = 3
"""
