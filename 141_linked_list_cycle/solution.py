
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Use a set to keep track of visited nodes.
    """

    def has_cycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        visited = set()

        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False


class Solution_2:
    """
    Use fast and slow pointer.
    """

    def has_cycle(self, head, ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

