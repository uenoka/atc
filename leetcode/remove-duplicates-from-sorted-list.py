# remove-duplicates-from-sorted-list.py
'''
めっちゃ基礎的なことかもだけど、なんで head を return すると OK になるんだ…?
current が参照を持っているだけだから、元のクラスを更新しているから?
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newHead = head
        while newHead != None and newHead.next != None:
            if newHead.next.val == newHead.val:
                newHead.next = newHead.next.next
            else:
                newHead = newHead.next
        return head
