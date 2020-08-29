# remove-duplicates-from-sorted-list-ii.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newHead = head
        while newHead != None and newHead.next != None:
            while newHead == newHead.next:
                newHead = newHead.next
                newHead.next = newHead.next.next
            newHead = newHead.next
        return head
