class Solution:
    def count_substrings(self, s: str):
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if j-1 >= i+1 else 1
                else:
                    dp[i][j] = 0

        res = 0
        for i in range(n):
            for j in range(i, n):
                res += dp[i][j]

        return res


"""
s = 'aaa', n = 3

dp =
    1 1 1
    0 1 1
    0 0 1

i = 2, j = 3
i = 1, j = 2
i = 0, j = 1
i = 0, j = 2

"""
