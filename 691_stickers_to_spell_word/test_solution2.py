from solution2 import min_stickers
import pudb


def test():
    stickers = ["notice", "possible"]
    # stickers = ["notice"]
    target = "basicbasic"
    # pudb.set_trace()
    res = min_stickers(stickers, target)
    assert res == -1
