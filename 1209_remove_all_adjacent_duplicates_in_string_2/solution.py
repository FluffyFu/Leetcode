def remove(s, k):
    stack = []

    for c in s:
        if not stack:
            stack.append((c,  1))
        elif stack[-1][0] == c:
            cnt = stack[-1][1]
            if cnt == k-1:
                stack.pop()
            else:
                stack[-1] = (c, 1+cnt)
        else:
            stack.append((c, 1))

    return ''.join(w[0] * w[1] for w in stack)

