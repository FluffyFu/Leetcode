class Solution:
    def valid_palindrome(self, s):
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        if left >= right:
            return True
        if s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]:
            return True
        return False


"""
s = 'aba', left = 0, right = 2
left = 1, right = 1

s = 'abca', left = 0, right = 3
left = 1, right = 2
"""

