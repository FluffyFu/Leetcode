from solution import mul
import pudb


def test_mul():
    num1 = "2"
    num2 = "3"

    # pudb.set_trace()
    res = mul(num1, num2)
    assert res == '6'

    num1 = "999"
    num2 = "99"
    # pudb.set_trace()
    res = mul(num1, num2)
    assert res == '56088'
