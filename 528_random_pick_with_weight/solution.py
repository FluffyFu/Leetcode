import random


class Solution:
    def __init__(self, w):
        self._cum_sum = [w[0]]
        for n in w[1:]:
            self._cum_sum.append(self._cum_sum[-1] + n)

    def pickIndex(self):
        val = random.randrange(1, self._cum_sum[-1]+1)
        return self._inverse_func(val)

    def _inverse_func(self, val):
        l, r = 0, len(self._cum_sum)

        while l <= r:
            mid = l + (r - l) // 2
            if self._cum_sum[mid] > val:
                r = mid - 1
            elif self._cum_sum[mid] < val:
                l = mid + 1
            else:
                l = mid

        return l

