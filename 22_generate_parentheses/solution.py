from typing import List


class Solution:
    """
    Use a stack to keep track if the parenthesis are valid.
    """

    def generate_parenthesis(self, n: int) -> List[str]:
        n_left = n
        n_right = n
        path = ''
        stack = []
        res = []

        self._back_track(n_left, n_right, stack, path, res)

        return res

    def _back_track(self, n_left: int, n_right: int, stack: List[str], path: str, res: List[List[str]]) -> None:
        if n_right == 0 and n_left == 0 and len(stack) == 0:
            res.append(path)
            return

        if n_left > 0:
            stack.append('(')
            self._back_track(n_left - 1, n_right, stack, path + '(', res)
            stack.pop()

        if n_right > 0 and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
            self._back_track(n_left, n_right - 1, stack, path + ')', res)
            stack.append('(')


class Solution_2:
    """
    In fact, we just need to check if the numbers of left parenthesis is greater
    than right parenthesis to determine if a right parenthesis is valid.
    """

    def generate_parenthesis(self, n: int) -> List[str]:
        res = []
        path = ''

        self._back_track(n, n, path, res)
        return res

    def _back_track(self, n_left: int, n_right: int, path: str, res: List[str]) -> None:
        if n_left == 0 and n_right == 0:
            res.append(path)

        if n_left > 0:
            self._back_track(n_left - 1, n_right, path + '(', res)
        if n_left < n_right:
            # there are more left parenthesis in the path, meaning it's okay to add right parenthesis.
            self._back_track(n_left, n_right - 1, path + ')', res)
