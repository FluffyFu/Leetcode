from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp) -> str:
        if key not in self.store:
            return ''

        # search for the index with timestamp smaller or equal to the given one
        vals = self.store[key]
        l = 0
        h = len(vals) - 1

        while l <= h:
            mid = l + (h-l) // 2

            if vals[mid][0] > timestamp:
                h = mid - 1
            elif vals[mid][0] < timestamp:
                l = mid + 1
            else:
                h = mid - 1

        if l == len(vals):
            # timestamp is larger than all the store vals
            return vals[-1][1]
        elif vals[l][0] == timestamp:
            # timestamp is equal to the one in the store
            return vals[l][1]
        elif vals[l][0] > timestamp and l > 0:
            # no equal timestamp, if there is previous one return that
            return vals[l-1][1]
        else:
            # otherwise there is no val smaller than the given timestamp
            return ''

