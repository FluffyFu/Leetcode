from typing import List


class Solution_2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._back_tracking(nums, [], res)
        return res

    def _back_tracking(self, nums, path, res):
        if not nums:
            res.append(path[:])  # append a copy of path to avoid mutable trap.
        for i in range(len(nums)):
            path = path + [nums[i]]
            self._back_tracking(nums[:i] + nums[i+1:], path, res)
            path.pop()

