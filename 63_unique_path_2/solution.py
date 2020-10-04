from typing import List


class Solution:
    def unique_path_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])

        if ((m == 1) or (n == 1)) and any((any(row) for row in obstacle_grid)):
            return 0

        if obstacle_grid[0][0] == 1 or obstacle_grid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for j in range(1, n):
            if obstacle_grid[0][j] == 0:
                dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            if obstacle_grid[i][0] == 0:
                dp[i][0] = dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
