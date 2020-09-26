from typing import List


class Solution:
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True
