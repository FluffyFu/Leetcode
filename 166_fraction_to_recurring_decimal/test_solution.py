from solution import fractionToDecimal
import pudb


def test_fractionToDecimal():
    numerator = 1
    denominator = 2
    # pudb.set_trace()
    res = fractionToDecimal(numerator, denominator)
    assert res == '0.5'

    numerator = 1
    denominator = 3
    # pudb.set_trace()
    res = fractionToDecimal(numerator, denominator)
    assert res == '0.(3)'

    numerator = -1
    denominator = 3
    # pudb.set_trace()
    res = fractionToDecimal(numerator, denominator)
    assert res == '-0.(3)'

    numerator = 4
    denominator = 333
    pudb.set_trace()
    res = fractionToDecimal(numerator, denominator)
    assert res == '0.(012)'
