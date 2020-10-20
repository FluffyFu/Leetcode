from collections import Counter


class Solution:
    def can_permute_palindrome(self, s):
        c = Counter(s)

        odd_cnts = 0
        for cnt in c.values():
            if cnt % 2 == 1:
                odd_cnts += 1

        return odd_cnts <= 1

