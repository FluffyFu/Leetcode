from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        cur_left, cur_right = intervals[0]

        for left, right in intervals[1:]:
            if left <= cur_right and right > cur_right:
                cur_right = right
            elif left > cur_right:
                res.append([cur_left, cur_right])
                cur_left = left
                cur_right = right

        res.append([cur_left, cur_right])  # append the last interval
        return res

    def merge_clean(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Same idea, more compact version.
        """
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res

