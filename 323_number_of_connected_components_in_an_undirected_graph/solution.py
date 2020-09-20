from typing import List, Set


class Solution:
    def count_components(self, n, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        graph = self._create_adjacent_list(n, edges)
        visited = set()
        res = 0
        for v in range(n):
            if not v in visited:
                self._dfs(v, visited, graph)
                res += 1

        return res

    def _create_adjacent_list(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Helper function to generate a map between a nod and its neighbors.
        """
        res = {i: [] for i in range(n)}

        for e in edges:
            v, w = e
            res[v].append(w)
            res[w].append(v)

        return res

    def _dfs(self, v: int, visited: Set[int], graph: List[List[int]]) -> None:
        visited.add(v)
        for w in graph[v]:
            if not w in visited:
                self._dfs(w, visited, graph)
