class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        cur = head

        while cur.next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        cur.next = pre
        return cur


class SolutionRecursive:
    def reverse_list(self, head):
        if not head:
            return None
        if not head.next:
            return head

        temp = head.next
        new_head = self.reverse_list(head.next)
        temp.next = head
        head.next = None

        return new_head
