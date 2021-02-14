def find(n):
    if n == 1:
        return ['1', '8', '0']
    elif n == 2:
        return ['11', '69', '88', '96']
    if n % 2 == 0:
        return [s[:n//2-1] + c + s[n//2-1:] for s in find(n-2) for c in ['11', '69', '88', '96', '00']]
    if n % 2 == 1:
        return [s[:(n-1)//2] + c + s[(n-1)//2:] for s in find(n-1) for c in ['1', '8', '0']]

