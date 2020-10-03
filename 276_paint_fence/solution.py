class Solution:
    def num_ways(self, n: int, k: int) -> int:
        """
        Let f(n) be the number of ways to paint the fence for n posts.
        f(n) can be decomposed into two parts, 1) the n-th and the (n-1)-th
        are different; 2) the n-th and (n-1)-th are the same, denoted by S(n)

        f(n) = f(n-1) * (k - 1) + S(n)

        Since n-th and (n-1)-th are the same, requires (n-2)-th and (n-1)-th should
        be different i.e.

        S(n) = f(n-2) * (k - 1)

        Therefore:
        f(n) = [f(n-1) + f(n-2)] * (k - 1)

        """
        if k == 0 or n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k**2

        pre = k
        cur = k**2
        for _ in range(3, n+1):
            temp = cur
            cur = (cur + pre) * (k - 1)
            pre = temp

        return cur

