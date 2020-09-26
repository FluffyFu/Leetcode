
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

        for _ in range(m-1):
            pre = cur
            cur = cur.next

        cur_temp = cur
        pre_temp = None

        for _ in range(n - m + 1):
            # the reverse operation takes (m -n) + 1 times.
            # when m == n, the operation does not change the original linked list.
            temp = cur_temp.next
            cur_temp.next = pre_temp
            pre_temp = cur_temp
            cur_temp = temp

        pre.next = pre_temp
        cur.next = cur_temp

        return dummy.next

