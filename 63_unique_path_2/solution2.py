class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid):
        n_row, n_col = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[0] * n_col for _ in range(n_row)]

        for i in range(n_col):
            if obstacle_grid[0][i] == 0:
                dp[0][i] = 1
            else:
                j = i
                while j < n_col:
                    dp[0][j] = 0
                    j += 1
                break

        for j in range(n_row):
            if obstacle_grid[j][0] == 0:
                dp[j][0] = 1
            else:
                i = j
                while i < n_row:
                    dp[i][0] = 0
                    i += 1
                break

        for i in range(1, n_row):
            for j in range(1, n_col):
                if obstacle_grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[n_row-1][n_col-1]


"""
[[0, 0, 0],
[0, 1, 0],
[0, 0, 0]]

dp =
[[1, 1, 1]
[1, 0, 1],
[1, 0, 0]]
"""

