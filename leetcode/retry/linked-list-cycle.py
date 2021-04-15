# linked-list-cycle.py

class Solution:
    def hasCycle(self, head) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
