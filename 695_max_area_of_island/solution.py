from typing import List


class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        res = 0
        n_cols = len(grid[0])
        n_rows = len(grid)

        for x in range(n_cols):
            for y in range(n_rows):
                if grid[y][x] == 1:
                    accumalate = self._dfs(
                        x, y, grid, n_rows, n_cols)
                    res = max(res, accumalate)
        return res

    def _dfs(self, x, y,  grid, n_rows, n_cols):
        if x < 0 or x >= n_cols or y < 0 or y >= n_rows or grid[y][x] != 1:
            return 0
        grid[y][x] = 0

        return (1 + self._dfs(x - 1, y, grid, n_rows, n_cols) +
                self._dfs(x + 1, y, grid, n_rows, n_cols) +
                self._dfs(x, y - 1, grid, n_rows, n_cols) +
                self._dfs(x, y + 1, grid, n_rows, n_cols))

