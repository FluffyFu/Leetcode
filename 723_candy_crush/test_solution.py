from solution import candy
import pudb


def test():
    board = [
            [1, 2, 1],
            [1, 1, 1]
    ]
    pudb.set_trace()
    assert candy(board) == [
        [0, 0, 0],
        [1, 2, 1]
    ]

