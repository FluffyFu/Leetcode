from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = []
        self._table = defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = val not in self._table

        # (val, the index of table[val])
        self._nums.append((val, len(self._table[val])))
        # the index of the newly appended val in nums
        self._table[val].append(len(self._nums)-1)

        return res

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self._table.get(val):
            return False
        else:
            n = len(self._nums)

            # the index in nums
            cur_index = self._table.get(val).pop()

            if cur_index == n - 1:
                self._nums.pop()
                return True

            # switch with the last element
            self._nums[cur_index], self._nums[n -
                                              1] = self._nums[n-1], self._nums[cur_index]
            self._nums.pop()

            # update the index of the switched element
            # this is why we also need to store the index in nums
            index_list = self._table[self._nums[cur_index][0]]
            index_list[self._nums[cur_index][1]] = cur_index
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self._nums)[0]
