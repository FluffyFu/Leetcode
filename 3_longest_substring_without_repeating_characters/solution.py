
class Solution:
    def len_longest_substring(self, s: str) -> int:
        """
        eager storage. current_letters is always accurate.
        """
        if not s:
            return 0

        res = 0
        current_letters = set()
        left = 0
        for right in range(len(s)):
            if not s[right] in current_letters:
                current_letters.add(s[right])
                if len(current_letters) > res:
                    res = len(current_letters)
            else:
                while s[left] != s[right]:
                    current_letters.remove(s[left])
                    left += 1
                left += 1
        return res

    def len_longest_substring_with_dict(self, s: str) -> int:
        """
        lazy storage. need to check with current left point when
        retrieving the index.
        """
        if not s:
            return 0
        letters_map = dict()

        res = 0
        left = 0
        for right in range(len(s)):
            if not s[right] in letters_map:
                letters_map[s[right]] = right
            else:
                # find the valid left pointer position
                left = max(letters_map[s[right]] + 1, left)
                letters_map[s[right]] = right
            if (right - left) + 1 > res:
                res = right - left + 1

        return res
