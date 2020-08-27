# linked-list-cycle.py
'''
問題文とインプットが分かったうえで、どういうことなのかがよくわからない。。。
input : 
ListNode : [1,3,2,4]
pos : 1
の場合は
ListNode の最後の要素と pos の要素が繋がっているというのを表現しているということ?
とすると普通に再帰か for で書いて今まで見た要素に当たったら終わりってすればいい?
要素数によってちょっと変わるけど
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        found = {}
        while head != None:
            if head in found:
                return True
            else:
                found[head] = 1
            head = head.next
        return False
