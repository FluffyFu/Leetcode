from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        slow = 0    # the elements before slow index are good to go.
        fast = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1

        return slow
