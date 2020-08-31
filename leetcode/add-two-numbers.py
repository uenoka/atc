class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# add-two-numbers.py
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2
        digit = 1
        dummy = ListNode(0)
        carry = 0
        while current1 and current2:
            newNode = ListNode((current1.val + current2.val + carry)*digit)
            carry = newNode.val//10
            current1 = current1.next
            current2 = current2.next
            digit += 1
        return dummy.next
