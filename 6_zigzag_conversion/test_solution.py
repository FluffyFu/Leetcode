from solution import Solution


def test_solution():
    s = "PAYPALISHIRING"
    num_rows = 3

    assert Solution().convert(s, num_rows) == "PAHNAPLSIIGYIR"

    s = "PAYPALISHIRING"
    num_rows = 4
    assert Solution().convert(s, num_rows) == "PINALSIGYAHRPI"

    s = 'A'
    num_rows = 1
    assert Solution().convert(s, num_rows) == "A"
