from solution import add_ops


def test():
    num = '123'
    target = 6
    res = add_ops(num, target)
    assert res == ['1+2+3', '1*2*3']

    num = '232'
    target = 8
    res = add_ops(num, target)
    assert res == ["2+3*2", "2*3+2"]

    num = '105'
    target = 5
    res = add_ops(num, target)
    assert res == ['1*0+5', '10-5']

    num = '00'
    target = 0
    res = add_ops(num, target)
    assert res == ['0+0', '0-0', '0*0']

    num = '123'
    target = 123
    res = add_ops(num, target)
    assert res == ['123']
