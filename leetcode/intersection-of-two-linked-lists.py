# intersection-of-two-linked-lists.py
import ListNode
'''
パッと見ではO(MN)解法しか出ない。
片方のListNodeを全部setに入れ込んでもう片方を1周すればO(N+M)で行ける？
''' 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headBset = set()
        while headB:
            headBset.add(headB)
            headB = headB.next
        print(headBset)
        while headA:
            print('current',headA.val)
            if headA in headBset:
                return headA
            headA = headA.next
        return None