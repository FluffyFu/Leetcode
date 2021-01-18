from solution import solve, diag
import pudb


def test():
    n = 1
    assert [['Q']] == solve(n)

    n = 4
    # pudb.set_trace()
    res = solve(n)
    print(res)
    assert len(res) == 2
    assert 0
