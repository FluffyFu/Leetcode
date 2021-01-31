from solution import helper, convert
import pudb


def test_helper():
    num = 23
    res = helper(num)
    assert res == 'Twenty Three'

    num = 123
    res = helper(num)
    assert res == 'One Hundred Twenty Three'

    num = 100
    res = helper(num)
    assert res == 'One Hundred'


def test_convert():
    num = 234
    res = helper(num)
    assert res == 'Two Hundred Thirty Four'

    num = 1234
    # pudb.set_trace()
    res = convert(num)
    assert res == 'One Thousand Two Hundred Thirty Four'

    num = 10000234
    res = convert(num)
    assert res == 'Ten Million Two Hundred Thirty Four'

    num = 10000
    res = convert(num)
    assert res == 'Ten Thousand'

    num = 50000
    res = convert(num)
    assert res == 'Fifty Thousand'

    num = 50868
    res = convert(num)
    assert res == 'Fifty Thousand Eight Hundred Sixty Eight'
