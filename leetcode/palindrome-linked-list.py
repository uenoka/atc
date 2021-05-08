# palindrome-linked-list.py
'''
うまいこと1回の探索でできないかと思ったが、長さが分からない中でやるのは相当難しいので断念。
簡単な方法だとListにそれぞれの値入れてListのほうを探索するやり方かな
deque でもできるけどそれはやってることは大して変わらない（書き方どっちがきれいかとかそのくらいかな）
基本はこれでACできるが time O(N), space O(1) の解法があるらしい。こっちはまたいずれ。
'''
import ListNode
from Util import createListNode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        for i in range(len(nodes)//2):
            # print(i,-i,nodes[i],nodes[-i-1])
            if not nodes[i] == nodes[-i-1]:
                return False
        return True

testcases = [
    [1,2,2,1],
    [1,2,3,2,1],
    [1,1,1,2,1,1],
    [1]
]
for nodes in testcases:
    print('testcase',nodes)
    head = createListNode().create(nodes)
    sol = Solution().isPalindrome(head)
    print(sol)