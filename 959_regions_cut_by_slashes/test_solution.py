from solution import cut
import pudb


def test():
    grid = [
        " /",
        "/ "
    ]
    # pudb.set_trace()
    assert 2 == cut(grid)

