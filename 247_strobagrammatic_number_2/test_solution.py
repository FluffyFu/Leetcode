from solution import find
import pudb


def test_find():
    # n = 2
    # res = find(n)
    # assert res == ['11', '69', '88', '96']

    n = 3
    # pudb.set_trace()
    res = find(n)
    print(res)
    assert res == ['11', '69', '88', '96']
