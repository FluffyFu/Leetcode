def validate(s):
    if not s:
        return True

    s = s.lower()
    data = [c for c in s if c.isalnum()]

    low, high = 0, len(data) - 1

    while low < high:
        if data[low] != data[high]:
            return False
        low += 1
        high -= 1

    return True

