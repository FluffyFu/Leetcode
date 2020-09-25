from typing import List


class Solution:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self._back_track(candidates, [], res, target)

        return self._remove_duplicates(res)

    def _back_track(self, candidates: List[int], path: List[int], res: List[List[int]], target) -> None:
        if sum(path) == target:
            res.append(path)
            return
        if sum(path) > target:
            return

        for num in candidates:
            self._back_track(candidates, path + [num], res, target)

    def _remove_duplicates(self, res: List[List[int]]):
        temp_set = set()
        for sub_res in res:
            temp_set.add(tuple(sorted(sub_res)))

        return [list(sub_res) for sub_res in temp_set]


class SolutionFast:
    """
    The above solution can be improved from two perspectives:
        - Redefine the recursive tree, so that there is no duplicates.
        - Update the target when a new element is added to the path to a
          avoid the sum in the end.
    """

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self._back_track(candidates, path, target, res)

        return res

    def _back_track(self, candidates: List[int], path: List[int], target: int, res: List[List]) -> None:
        if target == 0:
            res.append(path[:])
            return
        elif target < 0:
            return

        for i in range(len(candidates)):
            self._back_track(
                candidates[i:], path + [candidates[i]], target - candidates[i], res)

