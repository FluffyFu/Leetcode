from collections import Counter


class Solution:
    def longest_palindrome(self, s):
        c = Counter(list(s.lower()))

        n_even, n_odd = 0, 0
        contain_odd = 0

        for _, val in c.items():
            if val % 2 == 0:
                n_even += val
            else:
                n_odd += val - 1
                contain_odd = 1

        return n_even + n_odd + contain_odd


"""
s = 'abccccdd', c = {'a': 1, 'b': 1, 'c': 4, 'd': 2}
a, 1, n_odd = 1, n_even = 0
b, 1, n_odd = 1, n_even = 0
c, 4, n_odd = 1, n_even = 4
d, 2, n_odd = 1, n_even = 6
"""

