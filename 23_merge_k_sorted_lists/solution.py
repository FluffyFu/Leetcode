import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
O(log(k) * N)
"""


def merge(lists):
    if not lists:
        return None
    hq = []
    cnt = 0
    for node in lists:
        if node:
            heapq.heappush(hq, (node.val, cnt, node))
            cnt += 1
    dummy = ListNode()
    pre = dummy
    while hq:
        _, _, cur = heapq.heappop(hq)
        pre.next = cur
        pre = cur

        if cur.next:
            heapq.heappush(hq, (cur.next.val, cnt, cur.next))
            cnt += 1

    return dummy.next

