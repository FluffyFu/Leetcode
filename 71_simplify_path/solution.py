def simplify_path(path):
    path = path.split('/')

    stack = []
    for d in path:
        if d and d != '.' and d != '..' and d != '/':
            stack.append(d)
        elif d == '..' and stack:
            stack.pop()

    if not stack:
        return '/'
    else:
        return '/' + '/'.join(stack)

