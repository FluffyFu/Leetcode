class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Naive O(n) time and space
        """
        elements = []
        while head:
            elements.append(head.val)
            head = head.next

        low = 0
        high = len(elements) - 1

        while low <= high:
            if elements[low] == elements[high]:
                low += 1
                high -= 1
            else:
                return False
        return True


class Solution2:
    def is_palindrome(self, head):
        """
        O(1) space, O(n) time. Reverse the first half and compare it with the
        2nd half.
        """
        pre = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        if fast:
            slow = slow.next

        while pre and pre.val == slow.val:
            pre = pre.next
            slow = slow.next

        return not pre


"""
1 -> 2 -> 2 -> 1
None <- 1 <- 2
pre = None, fast = 1, slow = 1
fast = 2, temp = 2, pre = 1, slow = 2
fast = None, temp = 2, pre = 2, slow = 2

"""
