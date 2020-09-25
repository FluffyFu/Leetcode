
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        current = head

        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next

            current = current.next
        return head
