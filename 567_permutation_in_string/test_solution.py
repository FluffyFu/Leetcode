from solution import find_permutation, find_permutation_clean
import pudb


def test():
    s1 = 'ab'
    s2 = 'eidbaooo'

    assert find_permutation(s1, s2) == True
    # pudb.set_trace()
    assert find_permutation_clean(s1, s2) == True

    s1 = 'ab'
    s2 = 'eidboaoo'

    assert find_permutation_clean(s1, s2) == False
    assert find_permutation(s1, s2) == False

    s1 = 'adc'
    s2 = 'dcda'
    # pudb.set_trace()

    assert find_permutation_clean(s1, s2) == True
    assert find_permutation(s1, s2) == True

    s1 = 'hello'
    s2 = 'ooolleoooleh'
    # pudb.set_trace()

    assert find_permutation_clean(s1, s2) == False
    assert find_permutation(s1, s2) == False

