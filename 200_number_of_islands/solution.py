from typing import List, Set, Tuple


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n_rows = len(grid)
        n_cols = len(grid[0])

        visited = set()
        result = 0

        for x in range(n_cols):
            for y in range(n_rows):
                if (not (x, y) in visited) and grid[y][x] == '1':
                    self._dfs((x, y), visited, n_rows, n_cols, grid)
                    result += 1

        return result

    def _dfs(self, current: Tuple[int, int], visited: Set[Tuple[int, int]], n_rows: int, n_cols: int, grid) -> None:
        visited.add(current)

        for v in self._get_neighbor(current, n_rows, n_cols):
            x, y = v
            if (not v in visited) and (grid[y][x] == '1'):
                self._dfs(v, visited, n_rows, n_cols, grid)

    def _get_neighbor(self, current: Tuple[int, int], n_rows: int, n_cols: int) -> List[Tuple[int, int]]:
        x, y = current

        res = []

        if x - 1 >= 0:
            res.append((x - 1, y))
        if y + 1 < n_rows:
            res.append((x, y + 1))
        if x + 1 < n_cols:
            res.append((x + 1, y))
        if y - 1 >= 0:
            res.append((x, y - 1))

        return res


class Solution_2:
    """
    Modify the grid along the way to avoid saving visited points.
    """

    def num_islands(self, grid):
        if not grid:
            return 0
        res = 0

        n_rows = len(grid)
        n_cols = len(grid[0])

        for x in range(n_cols):
            for y in range(n_rows):
                if grid[y][x] == '1':
                    self._dfs(x, y, grid, n_rows, n_cols)
                    res += 1

        return res

    def _dfs(self, x, y, grid, n_rows, n_cols):
        if x >= n_cols or x < 0 or y >= n_rows or y < 0 or grid[y][x] != '1':
            return
        grid[y][x] = 0
        self._dfs(x + 1, y, grid, n_rows, n_cols)
        self._dfs(x - 1, y, grid, n_rows, n_cols)
        self._dfs(x, y - 1, grid, n_rows, n_cols)
        self._dfs(x, y + 1, grid, n_rows, n_cols)
