"""
Dijkstra's algorithm, use a max heap to keep track of the min value of the path
have seen so far.

Time: M*N * log(M*N)
"""
import heapq


def max_min_path(A):
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_q = [(-A[0][0], 0, 0)]

    nr, nc = len(A), len(A[0])

    while max_q:
        cur_v, i, j = heapq.heappop(max_q)
        if i == nr - 1 and j == nc - 1:
            return -cur_v
        for di, dj in dire:
            i_next = i + di
            j_next = j + dj

            if 0 <= i_next < nr and 0 <= j_next < nc and A[i_next][j_next] != -1:
                heapq.heappush(
                    max_q, (max(cur_v, -A[i_next][j_next]), i_next, j_next))
                A[i_next][j_next] = -1


"""
Union Find data structure. Percolation problem.
"""


def max_min_path2(A):
    uf = UnionFind(A)
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nr, nc = len(A), len(A[0])

    vals = []
    for i in range(nr):
        for j in range(nc):
            vals.append((A[i][j], i, j))

    vals = sorted(vals)

    start = 0
    end = nr * nc - 1
    visited = set()

    while vals:
        v, cur_i, cur_j = vals.pop()
        visited.add((cur_i, cur_j))

        for di, dj in dire:
            next_i = cur_i + di
            next_j = cur_j + dj

            if 0 <= next_i < nr and 0 <= next_j < nc and (next_i, next_j) in visited:
                uf.union(cur_i*nc + cur_j, next_i * nc + next_j)
        if uf.find(start) == uf.find(end):
            return v


class UnionFind:

    def __init__(self, A):
        self._nr = len(A)
        self._nc = len(A[0])
        self._p = [i for i in range(self._nr * self._nc)]

    def find(self, i):
        """
        path compression
        """
        if self._p[i] != i:
            self._p[i] = self.find(self._p[i])

        return self._p[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi != pj:
            # set one as the other's parent.
            self._p[pj] = pi

