def score(S):
    stack = []
    res = 0

    for c in S:
        if c == '(':
            stack.append(0)
        else:
            pre = stack.pop()
            # single parenthesis
            if pre == 0:
                temp = 1
            # recursive parenthesis
            else:
                temp = 2 * pre

            if not stack:
                res += temp
            else:
                stack[-1] = stack[-1] + temp
    return res


def score_2(S):
    """
    Post order traverse.
    https://leetcode.com/problems/score-of-parentheses/discuss/141777/C%2B%2BJavaPython-O(1)-Space
    """

    stack = []
    cur = 0

    for c in S:
        if c == '(':
            stack.append(cur)
            cur = 0
        else:
            if cur == 0:
                cur = 1
            else:
                cur = 2 * cur
            cur += stack.pop()
    return cur
