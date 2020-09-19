
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursion limit reached.
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        if n > 0:
            return x * self.myPow(x, n-1)
        if n < 0:
            return 1 / x * self.myPow(x, n+1)


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0

        sign = 1 if n > 0 else -1

        result = 1
        n = abs(n)

        lookup_table = {}
        res = self._power(x, n, lookup_table)

        return res if sign == 1 else 1 / res

    def _power(self, x: float, n: int, lookup_table: dict) -> float:
        """
        Helper function to calculate exponential with positive power.
        """
        if n == 0:
            return 1.0
        if n in lookup_table:
            return lookup_table[n]
        else:
            if n % 2 == 0:
                res = self._power(x, n/2, lookup_table) * \
                    self._power(x, n/2, lookup_table)
            else:
                res = self._power(x, n-1, lookup_table) * x

            lookup_table[n] = res
            return res
