from solution import reconstruct
import pudb


def test_reconstruct():
    org = [1, 2, 3]
    seqs = [[1, 2],
            [1, 3],
            [2, 3]]
    # pudb.set_trace()
    assert reconstruct(org, seqs) == True

    org = [1]
    seqs = [[1],
            [1],
            [1]]
    assert reconstruct(org, seqs) == True

    org = [1, 2, 3, 4, 5]
    seqs = [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1], [4], [5]]
    assert reconstruct(org, seqs) == True

    org = [1]
    seqs = [[1], [2, 3], [3, 2]]
    assert reconstruct(org, seqs) == False

