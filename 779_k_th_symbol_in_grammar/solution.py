
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = self._dfs(k)
        return 1 if res == 1 else 0

    def _dfs(self, k: int) -> int:
        if k == 1:
            return 0
        if k % 2 == 0:
            return 1 - self._dfs(k/2)  # flip between 1 and 0
        else:
            return self._dfs((k+1)/2)
