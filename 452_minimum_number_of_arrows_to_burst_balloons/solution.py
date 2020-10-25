class Solution:
    def find_min_arrow_shots(self, points):
        if not points:
            return 0
        points = sorted(points, key=lambda x: x[0])

        h = points[0][1]

        res = 1
        for p in points[1:]:
            if p[0] > h:
                h = p[0]
                res += 1
            else:
                h = min(h, p[0])

        return res


"""
[[1, 6], [2, 8], [7, 12], [10, 16]]

l = 1, h = 6, res = 1

new_l = 2, new_h = 8, l = 2, h = 6
new_l = 7, new_h = 12, l = 7, h = 12, res = 2
new_l = 10, new_h = 16, l = 10, h = 12, res = 2
"""

