from solution3 import is_sorted
import pudb


def test():
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    res = is_sorted(words, order)
    assert res == True
