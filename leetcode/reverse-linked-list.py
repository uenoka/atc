# reverse-linked-list.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            current = head
            head = head.next
            current.next = pre
            pre = current
        return pre
