class Solution:
    def min_remove_to_make_valid(self, s):
        left_cnts = 0
        invalid_pos = []
        potential_invalid_pos = []
        for i, c in enumerate(s):
            if c == ')' and left_cnts == 0:
                invalid_pos.append(i)
            elif c == ')' and left_cnts > 0:
                left_cnts -= 1
            elif c == '(':
                left_cnts += 1
                potential_invalid_pos.append(i)

        if left_cnts > 0:
            invalid_pos += potential_invalid_pos[-left_cnts:]

        res = []
        for i in range(len(s)):
            if i in invalid_pos:
                continue
            res.append(s[i])

        return ''.join(res)

    def min_remove_to_make_valid_2(self, s):
        stack = []
        s = list(s)

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        while stack:
            s[stack.pop()] = ''

        return ''.join(s)


"""
s = 'a)b(c)d'
i = 0, c = 'a', i = 1, 'c' = ')', invalid_pos = [1]
i = 2, c = 'b',
i = 3, c = '(', left_cnts = 1, p_pos = [3], i_pos = [1]
i = 4, c = 'c',
i = 5, c = ')', left_cnts = 0
"""

