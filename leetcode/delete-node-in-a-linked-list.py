# delete-node-in-a-linked-list.py
'''
single linked list は前の node の情報を自信は持っていないので、自信の値を次の node の値に書き換えて、参照先を1つ飛ばすという解法になる。
double linked list であれば、前の node の next を 次の node に書き換えるといい。おそらく↓のような感じ

class Solution:
    def deleteNode(self, node):
        node.prev.next = node.next

'''


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
