from solution import max_min_path2, UnionFind
import pudb


def test():
    A = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    # pudb.set_trace()
    res = max_min_path2(A)
    assert res == 4


def test_uf():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # pudb.set_trace()
    uf = UnionFind(A)
    uf._p = [0, 1, 2, 3, 4, 2, 7, 7, 5]
    uf.union(7, 8)

