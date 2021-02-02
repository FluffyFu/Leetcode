from solution import is_number


def test():
    nums = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
            "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for s in nums:
        res = is_number(s)
        # print(s)
        assert res == True

    neg_nums = ['4e+', '.e1', "abc", "1a", "1e", "e3",
                "99e2.5", "--6", "-+3", "95a54e53"]

    for s in neg_nums:
        res = is_number(s)
        print(s)
        assert res == False

