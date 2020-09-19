from solution import Solution


def test_solution():
    n, k = 1, 1
    assert Solution().kthGrammar(n, k) == 0

    n, k = 2, 1
    assert Solution().kthGrammar(n, k) == 0

    n, k = 2, 2
    assert Solution().kthGrammar(n, k) == 1

    n, k = 4, 5
    assert Solution().kthGrammar(n, k) == 1
