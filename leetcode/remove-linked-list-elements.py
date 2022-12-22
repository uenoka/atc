# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Util import createListNode
from ListNode import ListNode
from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        dummy = head
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy


sol = Solution()
head = createListNode().create([1,2,6,3,4,5,6])
n = 6
print(sol.removeElements(head, n))
