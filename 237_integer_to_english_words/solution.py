under_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
        'Sixty', 'Seventy', 'Eighty', 'Ninety']
thousands = ['', 'Thousand', 'Million', 'Billion']


def convert(num):
    if num == 0:
        return 'Zero'
    res = ''

    for i in range(len(thousands)):
        if num % 1000 != 0:
            res = helper(num % 1000) + ' ' + thousands[i] + ' ' + res
        num = num // 1000

    return res.strip()


def helper(num):
    """
    Convert a string of integer of length from 1-3 to English word.
    """
    if num < 20:
        return under_20[num]
    elif num < 100:
        return (tens[num // 10] + ' ' + under_20[num % 10]).strip()
    else:
        return (under_20[num // 100] + ' Hundred ' + helper(num % 100)).strip()
