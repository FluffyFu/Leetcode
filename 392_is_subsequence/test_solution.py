from solution import Solution
import pudb


def test_solution():
    s = 'abc'
    t = 'ahbgdc'
    assert Solution().is_subsequence(s, t) == True
    assert Solution().is_subsequence_iterative(s, t) == True
    assert Solution().is_subsequence_iterative_clean(s, t) == True
    pudb.set_trace()
    assert Solution().is_subsequence_streaming(s, t) == True

    s = 'axc'
    t = 'ahbgdc'
    assert Solution().is_subsequence(s, t) == False
    assert Solution().is_subsequence_iterative(s, t) == False
    assert Solution().is_subsequence_iterative_clean(s, t) == False
    assert Solution().is_subsequence_streaming(s, t) == False
