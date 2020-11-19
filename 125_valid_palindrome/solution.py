class Solution:

    def is_palindrome(self, s):
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


"""
"race a car"
left = 0, right = 9
left = 1, right = 8
left = 2, right = 7
left = 3, right = 6
left = 3, right = 5
"""
