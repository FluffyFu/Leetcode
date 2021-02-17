from solution import add_bold


def test():
    s = "abcxyz123"
    dictionary = ["abc", "123"]
    res = add_bold(s, dictionary)
    assert res == "<b>abc</b>xyz<b>123</b>"

    s = "aaabbcc"
    dictionary = ["aaa", "aab", "bc"]
    res = add_bold(s, dictionary)
    assert res == "<b>aaabbc</b>c"

