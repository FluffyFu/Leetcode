
class Solution:
    def two_sum(self, nums, target) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target - num], i]
            else:
                index_map[num] = i
