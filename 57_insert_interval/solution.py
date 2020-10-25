class Solution:
    def insert(self, intervals, new_interval):
        res = []
        new_low, new_high = new_interval

        for i in range(len(intervals)):
            if intervals[i][1] < new_low:
                res.append(intervals[i])
            elif intervals[i][0] > new_high:
                res.append([new_low, new_high])
                res += intervals[i:]
                return res
            else:
                new_low = min(new_low, intervals[i][0])
                new_high = max(new_high, intervals[i][1])

        res.append([new_low, new_high])

        return res


"""
intervals = [[1, 5]], new_interval = [2, 3]
new_low = 2, new_high = 3
i = 0

intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
new_low = 2, new_high = 5

i = 0, new_low = 1, new_high = 5
i = 1, res = [[1, 5], [6, 9]]
"""

