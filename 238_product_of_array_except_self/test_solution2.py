from solution2 import product, product_space_efficient
import pudb


def test_product():
    nums = [1, 2, 3, 4]
    # pudb.set_trace()
    res = product_space_efficient(nums)
    assert res == [24, 12, 8, 6]
