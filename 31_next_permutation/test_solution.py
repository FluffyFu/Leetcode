from solution import Solution
import pudb


def test_solution():
    a = [1, 2, 3]
    Solution().next_permutation(a)
    assert a == [1, 3, 2]


def test_solution_2():
    a = [3, 2, 1]
    Solution().next_permutation(a)
    assert a == [1, 2, 3]


def test_solution_3():
    a = [3, 4, 1]
    # pudb.set_trace()
    Solution().next_permutation(a)
    assert a == [4, 1, 3]


def test_solution_4():
    a = [2, 3, 1]
    Solution().next_permutation(a)
    assert a == [3, 1, 2]


def test_solution_5():
    a = [1, 3, 2]
    Solution().next_permutation(a)
    assert a == [2, 1, 3]


def test_reverse_list():
    a = [4, 3, 2, 1]
    Solution()._reverse_list(a, left=1, right=3)
    assert a == [4, 1, 2, 3]
