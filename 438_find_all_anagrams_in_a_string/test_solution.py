from solution import Solution
import pudb


def test_solution():
    s = 'cbaeabc'
    p = 'abc'
    # pudb.set_trace()
    assert Solution().find_anagrams_fast(s, p) == [0, 4]

    s = 'abab'
    p = 'ab'
    assert Solution().find_anagrams_fast(s, p) == [0, 1, 2]

    s = 'baa'
    p = 'aa'
    assert Solution().find_anagrams_fast(s, p) == [1]

