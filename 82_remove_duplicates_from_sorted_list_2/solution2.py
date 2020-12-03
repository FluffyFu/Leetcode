class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head

        while cur:
            dp = 0
            while cur.next and cur.val == cur.next.val:
                dp += 1
                cur = cur.next
            if dp > 0:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return dummy.next


"""
-1 -> 1 -> 3 -> 3 -> 5
pre = -1, cur = 1, dp = 0, pre = 1, cur = 3
dp = 0, dp = 1, cur = 3 (second), 1 -> 5
pre = 1, cur = 5

-1 -> 1 -> 1 -> 2 -> 3
pre = -1, cur = 1, dp = 1, cur = 1 (second), -1 -> 2 -> 3
pre = -1, cur = 2, pre = 2, cur = 3
"""

