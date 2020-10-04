class Solution:
    def unique_path(self, m: int, n: int) -> int:
        """
        O(n*m) space
        """
        if m == 1 or n == 1:
            return 1

        # dp[i][j] is the i-th row and j-th column
        dp = [[0] * n for _ in range(m)]

        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]

    def unique_path_less_space(self, m: int, n: int) -> int:
        """
        Instead of using m rows in the dp matrix, we only need to
        maintain one row. O(n) sapce
        """
        if m == 1 or n == 1:
            return 1
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]

        return dp[-1]
