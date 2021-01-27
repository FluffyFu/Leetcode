from solution import score, score_2
import pudb


def test():
    S = "()"
    res = score(S)
    assert res == 1
    assert score(S) == score_2(S)

    S = '(())'
    # pudb.set_trace()
    res = score_2(S)
    assert res == 2

    S = '()()'
    res = score(S)
    assert res == 2
    assert score(S) == score_2(S)

    S = '(()(()))'
    res = score(S)
    assert res == 6
    assert score(S) == score_2(S)
