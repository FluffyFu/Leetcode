from typing import List, Set


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = self._iterative_method(nums)

        return res

    def _back_track_post_order(self, nums: List[int], path: List[int], res: List[List[int]]):
        """
        The decision at each level is whether to take the i-th element. The results are the leaves.
        Therefore this solution is a post-order solution.

                        start
                        /  \ if  1 is selected
                    [1]     []
                   /  \    /  \  if 2 is selected
                [1, 2] [1] [2] []
               /    \   /\  /\  /\  if 3 is selected
            [1,2,3] [1,2] [1, 3] [1], [2, 3], [2], [3], []
        """
        if not nums:
            res.append(path)
            return

        self._back_track_post_order(nums[1:], path + [nums[0]], res)
        self._back_track_post_order(nums[1:], path, res)

    def _back_track_pre_order(self, nums: List[int], path: List[int], res: List[List[int]]):
        """
        The decision tree is pre-order is to build by considering using the i-th element(must appear)
        and its following elements.

                                []
                        /        |       \
                    [1]          [2]      [3]
                /    |            \
            [1, 2]  [1, 3]        [2, 3]
            /
         [1, 2, 3]
        """
        res.append(path)
        for i in range(len(nums)):
            self._back_track_pre_order(nums[i+1:], path + [nums[i]], res)

    def _iterative_method(self, nums: List[int]):
        res = [[]]
        for num in nums:
            res += [sub_res + [num] for sub_res in res]
        return res
