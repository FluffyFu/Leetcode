class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k**2

        res = k**2
        for _ in range(3, n+1):
            res = (k**2 - 1) * res / k

        return res

