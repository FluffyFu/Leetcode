class Solution:
    def min_available_duration(self, slots1, slots2, duration):
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)

        n1 = len(slots1)
        n2 = len(slots2)

        i = 0
        j = 0
        while i < n1 and j < n2:
            l1, h1 = slots1[i]
            l2, h2 = slots2[j]

            low = max(l1, l2)
            high = min(h1, h2)

            if high - low >= duration:
                return [low, low + duration]
            elif h1 >= h2:
                j += 1
            else:
                i += 1

        return []


"""
slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 12
n1 = 3, n2 = 2
i = 0, j = 0, l1 = 10, h1 = 50, l2 = 0, h2 = 15, low = 10, high = 15
i = 0, j = 1, l1 = 10, h1 = 50, l2 = 60, h2 = 70, low = 60, high = 50
i = 1, j = 1, l1 = 60, h1 = 120, l2 = 60, h2 = 70, low = 60, high = 70
i = 1, j = 2, return []


slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 8
n1 = 3, n2 = 2

i = 0, j = 0, l1 = 10, h1 = 50, l2 = 0, h2 = 15, low = 10, high = 15
i = 0, j = 1, l1 = 10, h1 = 50, l2 = 60, h2 = 70, low = 60, high = 50
i = 1, j = 1, l1 = 60, h1 = 120, l2 = 60, h2 = 70, low = 60, high = 70, return [60, 68]
"""

