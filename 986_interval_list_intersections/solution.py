class Solution:
    def interval_intersection(self, A, B):
        n1, n2 = len(A), len(B)
        i, j = 0, 0
        res = []

        while i < n1 and j < n2:
            l1, h1 = A[i]
            l2, h2 = B[j]

            inter_l = max(l1, l2)
            inter_h = min(h1, h2)

            if inter_l <= inter_h:
                res.append([inter_l, inter_h])
            if h1 >= h2:
                j += 1
            else:
                i += 1
        return res


"""
A = [[0, 2], [5, 10], [13, 23], [24, 25]], B = [[1, 5], [8, 12], [15, 24], [25, 26]]
n1 = 4, n2 = 4
i = 0, j = 0, l1 = 0, h1 = 2, l2 = 1, h2 = 5, inter_l = 1, inter_h = 2, res = [[1,2]]
i = 1, j = 0, l1 = 5, h1 = 10, l2 = 1, h2 = 5, inter_l = 5, inter_h = 5, res = [[1,2], [5, 5]]
i = 1, j = 1, l1 = 5, h1 = 10, l2 = 8, h2 = 12, inter_l = 8, inter_h = 10, res = [[1,2], [5,5], [8,10]]
i = 2, j = 1, l1 = 13, h1= 23, l2 = 8, h2 = 12, inter_l = 13, inter_h = 12, res = [[1,2], [5,5], [8,10]]
i = 2, j = 2, l1 = 13, h1= 23, l2 = 15, h2 =24, inter_l = 15, inter_h = 23, res = [[1,2], [5,5], [8,10], [15,23]]
i = 3, j = 2, l1 = 24, h1 =25, l2 = 15, h2 = 24, inter_l = 24, inter_h = 24, res = [[1,2], [5,5], [8,10], [15,23], [24,24]]
i = 3, j = 3, l1 = 24, h1= 25, l2 = 25, h2 = 26, inter_l = 25, inter_h = 25, res = [[1,2], [5,5], [8, 10], [15, 23], [24,24], [25,25]]
"""
