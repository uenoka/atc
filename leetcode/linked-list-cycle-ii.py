# linked-list-cycle-ii.py
# Definition for singly-linked list.
'''
linked-list-cycle をやった後だとすぐできるが、これをぱっと出されて出来るかというと微妙…
LinkedList はAtCoder だとあまり出ないし、結構苦手かも。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        found = {}
        while head != None:
            if head in found:
                return head
            else:
                found[head] = 1
            head = head.next
        return None
