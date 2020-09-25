
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while cur1 or cur2 or carry:
            if not cur1:
                cur1_val = 0
            else:
                cur1_val = cur1.val

            if not cur2:
                cur2_val = 0
            else:
                cur2_val = cur2.val

            carry, cur_val = divmod(cur1_val + cur2_val + carry, 10)

            cur.next = ListNode(cur_val)
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy.next


class SolutionRecursive:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self._add_two_numbers(l1, l2, 0)

    def _add_two_numbers(self, l1, l2, carry):
        if (not l1) and (not l2):
            if carry == 1:
                return ListNode(1)
            else:
                return None
        if not l1:
            if carry == 1:
                return self._add_two_numbers(l2, ListNode(1), 0)
            else:
                return l2
        if not l2:
            if carry == 1:
                return self._add_two_numbers(l1, ListNode(1), 0)
            else:
                return l1

        l1_val = l1.val + l2.val + carry

        if l1_val >= 10:
            l1_val -= 10
            carry = 1
        else:
            carry = 0

        l1.val = l1_val

        l1.next = self._add_two_numbers(l1.next, l2.next, carry)

        return l1


class SolutionRecursive2():
    """
    Simpler base case.
    """

    def add_two_numbers(self, l1, l2):
        if (not l1) and (not l2):
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        cur_val = l1.val + l2.val
        head = ListNode(cur_val % 10)

        head.next = self.add_two_numbers(l1.next, l2.next)
        if cur_val >= 10:
            head.next = self.add_two_numbers(head.next, ListNode(1))

        return head
