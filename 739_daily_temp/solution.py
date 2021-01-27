def find_days(T):
    res = [0] * len(T)
    stack = []

    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            res[cur] = i - cur

        stack.append(i)

    return res

