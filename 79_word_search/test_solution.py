from solution import search
import pudb


def test():
    board = [['a', 'a']]
    word = 'aaa'
    # pudb.set_trace()

    assert False == search(board, word)

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    pudb.set_trace()

    assert True == search(board, word)
