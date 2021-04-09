from Util import createListNode
from ListNode import ListNode

# add-two-numbers.py
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p = l1
        q = l2
        current = dummyHead
        carry = 0
        while p is not None or q is not None:
            x = 0 if p is None else p.val
            y = 0 if q is None else q.val
            sum = carry + x + y
            carry = sum//10
            current.next = ListNode(sum%10)
            current = current.next
            x = 0 if p is None else p.val
            if p is not None: p = p.next
            if q is not None: q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummyHead.next

l1 = [1,2,3,4,5]
l2 = [4,5,6]
l1node = createListNode().create(l1)
l2node = createListNode().create(l2)
print('=== l1 node ===')
createListNode().printNode(l1node, 0)
print('=== l2 node ===')
createListNode().printNode(l2node, 0)

sol = Solution().addTwoNumbers(l1node,l2node)
print('=== solution node ===')
createListNode().printNode(sol,0)
