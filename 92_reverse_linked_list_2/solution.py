
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1

        cur_temp = cur
        pre_temp = None

        while n > 0:
            temp = cur_temp.next
            cur_temp.next = pre_temp
            pre_temp = cur_temp
            cur_temp = temp
            n -= 1

        pre.next = pre_temp
        cur.next = cur_temp

        return dummy.next

