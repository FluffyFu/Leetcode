from typing import List


class Solution:
    def remove_covered_intervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # ascending order on the start and descending order on the end
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        cur_left, cur_right = intervals[0]

        n_overlap = 0

        for interval in intervals[1:]:
            left, right = interval

            if cur_right >= right:
                n_overlap += 1

            elif cur_right >= left and cur_right < right:
                cur_right = right  # combine the two intervals

            elif cur_right < left:
                # update current interval
                cur_left = left
                cur_right = right

        return len(intervals) - n_overlap
