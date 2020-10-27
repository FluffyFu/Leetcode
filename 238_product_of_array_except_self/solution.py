class Solution:
    def product_except_self(self, nums):
        """
        O(n) time without division.
        """
        pre_product = []
        p = 1
        for n in nums:
            pre_product.append(p)
            p *= n

        post_product = []
        p = 1
        for n in nums[::-1]:
            post_product.append(p)
            p *= n

        res = []
        for pre, post in zip(pre_product, post_product[::-1]):
            res.append(pre * post)
        return res

    def product_except_self_less_space(self, nums):
        """
        Without building the post_product list, modify in place.
        """
        res = []
        p = 1

        for n in nums:
            res.append(p)
            p *= n

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res


"""
[1, 2 ,3]
p = 1, n = 1, pre_product = [1], p = 1
p = 1, n =2, pre_product = [1, 1], p = 2
p = 2, n = 3, pre_product = [1, 1, 2], p = 6

p = 1, n = 3, post_product = [1], p = 3
p = 3, n = 2, post_product = [1, 3], p = 6
p = 6, n =1, post_product = [1, 3, 6], p = 6


"""
