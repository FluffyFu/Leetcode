class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []

        low = intervals[0][0]
        high = intervals[0][1]

        for new_low, new_high in intervals[1:]:
            if new_low > high:
                res.append([low, high])
                low = new_low
                high = new_high
            else:
                high = max(high, new_high)

        res.append((low, high))

        return res


"""
[[1, 3], [2, 6], [8, 10], [15, 18]]

low = 1, high = 3
new_low = 2, new_high = 6, low = 1, high = 6
new_low = 8, new_high = 10, res = [[1,6]], low = 8, high = 10
new_low = 15, new_high = 18, res = [[1, 6], [8, 10]], low = 15, high = 18
res = [[1, 6], [8, 10], [15, 18]]
"""
