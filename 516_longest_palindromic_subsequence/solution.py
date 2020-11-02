class Solution:
    def longest_subsequence(self, s):
        # dp[i][j] is length of LS of s[i:j+1], the final result is dp[0][len(s)-1]
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][n-1]


"""
s = 'cbbd', n = 4,
dp =
     1 1 2 2
     0 1 2 2
     0 0 1 1
     0 0 0 1
i = 3,
i = 2, j = 3, b != d
i = 1, j = 2, b == b
i = 1, j = 3, b != d
i = 0, j = 1, c != b
i = 0, j = 2

"""

