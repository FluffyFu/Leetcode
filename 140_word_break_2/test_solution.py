from solution import Solution, Solution2
import pudb


def test_solution():
    s = 'catsanddog'
    word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
    # pudb.set_trace()
    res = Solution().word_break(s, word_dict)
    assert res == ["cat sand dog", "cats and dog"]


def test_solution_2():
    s = 'catsanddog'
    word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
    # pudb.set_trace()
    res = Solution2().word_break(s, word_dict)
    print(res)
    assert res == ["cat sand dog", "cats and dog"]
