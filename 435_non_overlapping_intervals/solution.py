class Solution:
    def erase_overlap_intervals(self, intervals):
        end = -float('inf')
        res = 0

        for interval in sorted(intervals, key=lambda x: x[1]):
            if interval[0] >= end:
                end = interval[1]
            else:
                res += 1

        return res
