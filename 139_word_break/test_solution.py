from solution import Solution, Solution_2, Solution_3, Solution_4
import pudb


def test_solution():
    word_dict = {'aa', 'aaa'}
    s = 'aaa'
    pudb.set_trace()
    assert Solution().word_break(s, word_dict) == True


def test_solution_2():
    word_dict = {'aa', 'aaa'}
    s = 'aaa'
    # pudb.set_trace()
    assert Solution_2().word_break(s, word_dict) == True

    word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
                 "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    assert Solution_2().word_break(s, word_dict) == False


def test_solution_3():
    word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
                 "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    assert Solution_3().word_break(s, word_dict) == False


def test_solution_4():
    word_dict = {'aa', 'aaa'}
    s = 'aaa'
    # pudb.set_trace()
    assert Solution_4().word_break(s, word_dict) == True
