from solution import Solution
import pudb


def test_solution():
    accounts = [['John', 'A', 'B', 'C'],
                ['John', 'D', 'E'],
                ['John', 'A', 'F'],
                ['John', 'E', 'G']]
    # pudb.set_trace()
    res = Solution().account_merge(accounts)
    print(res)
    assert 0
