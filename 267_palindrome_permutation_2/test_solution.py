from solution import Solution
import pudb


def test_solution():
    s = 'aabb'
    # pudb.set_trace()
    res = Solution().generate_palindromes(s)
    assert res == ['abba', 'baab']

    s = 'aaa'
    # pudb.set_trace()
    res = Solution().generate_palindromes(s)
    assert res == ['aaa']

