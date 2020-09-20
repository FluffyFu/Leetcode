from solution import Solution
import pudb


def test_solution():
    s = 'abcabcbb'
    assert Solution().len_longest_substring(s) == 3

    s = 'bbbbb'
    assert Solution().len_longest_substring(s) == 1

    s = 'pwwkew'
    assert Solution().len_longest_substring(s) == 3

    s = 'abcabcbb'
    assert Solution().len_longest_substring_with_dict(s) == 3

    s = 'bbbbb'
    assert Solution().len_longest_substring_with_dict(s) == 1

    s = 'pwwkew'
    assert Solution().len_longest_substring_with_dict(s) == 3

    s = 'abba'
    assert Solution().len_longest_substring_with_dict(s) == 2
