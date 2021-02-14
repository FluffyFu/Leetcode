c_map = {
    '0': '0',
    '1': '1',
    '6': '9',
    '9': '6',
    '8': '8'
}


def check(num):
    if not num:
        return False
    for i in range(len(num)//2 + 1):
        if num[i] not in c_map or num[len(num) - i - 1] not in c_map or num[i] != c_map[num[len(num) - i - 1]]:
            return False
    return True

