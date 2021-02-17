def remove_dup(s):
    stack = []
    i = 0

    while i < len(s):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        i += 1
    return ''.join(stack)

