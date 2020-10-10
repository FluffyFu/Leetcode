from solution import Solution
import pudb


def test_solution():
    word_dict = {'aa', 'aaa'}
    s = 'aaa'
    pudb.set_trace()
    assert Solution().word_break(s, word_dict) == True
