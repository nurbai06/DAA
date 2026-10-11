class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        visited = set()
        current = headA
        while current is not None:
            visited.add(current)
            current = current.next

        current = headB
        while current is not None:
            if current in visited:
                return current
            current = current.next
        return None
