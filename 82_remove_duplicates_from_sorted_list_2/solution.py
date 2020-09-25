class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next

        while cur and cur.next:
            # we maintain the iteration in such a way that
            # each iteration, cur starts from a new number.

            if cur.next.val == cur.val:
                # this number has duplicates
                # proceeds until the next one
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                cur = cur.next
                # this is not the final link, because the new cur could
                # have duplicates too. But since we didn't change pre,
                # we can still change it later.
                pre.next = cur

            else:
                # cur does not have duplicates. proceed both pre and cur.
                pre = cur
                cur = cur.next

        return dummy.next


class SolutionRecursive:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next and head.next.val == head.val:
            while head.next and head.next.val == head.val:
                head = head.next
            head = head.next
            self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head
