def decode(s):
    cur_s = ""
    k = 0
    stack = []

    for c in s:
        if c.isdigit():
            k = k * 10 + int(c)

        elif c == '[':
            # start a new frame
            stack.append((cur_s, k))
            cur_s = ''
            k = 0
        elif c == ']':
            last_s, last_k = stack.pop()
            cur_s = last_s + last_k * cur_s
        else:
            cur_s += c
    return cur_s

