
class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' or c == ']' or c == '}':
                if len(stack) == 0:
                    return False
                if c == ')' and stack.pop() != '(':
                    return False
                if c == ']' and stack.pop() != '[':
                    return False
                if c == '}' and stack.pop() != '{':
                    return False

        return True if len(stack) == 0 else False

    def is_valid_clean(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in pairs:
                stack.append(c)
            elif c in pairs.values():
                if (len(stack) == 0) or pairs[stack.pop()] != c:
                    return False

        return len(stack) == 0
