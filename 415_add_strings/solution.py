class Solution:
    def add_string(self, num1: str, num2: str) -> str:
        num1 = self._convert_str_to_int(num1)
        num2 = self._convert_str_to_int(num2)

        res = num1 + num2
        return ''.join(list(str(res)))

    def _convert_str_to_int(self, num):
        res = 0
        for c in num:
            res = res * 10 + ord(c) - ord('0')

        return res


class Solution2:
    """
    Operate the digits directly.
    """

    def add_string(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)

        res = []
        carry = 0
        while num1 or num2:
            if num1:
                n1 = ord(num1.pop()) - ord('0')
            else:
                n1 = 0

            if num2:
                n2 = ord(num2.pop()) - ord('0')
            else:
                n2 = 0

            carry, cur = divmod(n1 + n2 + carry, 10)
            res.append(str(cur))
        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])


"""
num1 = '98', num2 = '9'

res = 0,
c = 9, res = 9
c = 8, res = 98
"""

