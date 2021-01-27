def flatten(array):
    res = []
    for e in array:
        if isinstance(e, int):
            res.append(e)
        else:
            res += flatten(e)

    return res


def flatten2(array):
    res = []
    stack = []

    stack = array[::-1]

    while stack:
        top = stack.pop()
        if isinstance(top, int):
            res.append(top)
            continue
        stack = stack[:-1] + top[::-1]

    return res


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self._res = []
#         for e in nestedList:
#             self._res += self._flatten(e)

#         self._cnt = 0

#     def _flatten(self, nest_int):
#         res = []
#         if nest_int.isInteger():
#             res.append(nest_int.getInteger())
#         else:
#             for e in nest_int.getList():
#                 res += self._flatten(e)
#         return res

#     def next(self) -> int:
#         cur = self._res[self._cnt]
#         self._cnt += 1
#         return cur

#     def hasNext(self) -> bool:
#         return self._cnt < len(self._res)
