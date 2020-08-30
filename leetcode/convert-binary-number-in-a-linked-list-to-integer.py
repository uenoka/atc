# convert-binary-number-in-a-linked-list-to-integer.py
'''
愚直な解法だったら、linked list が最後になるまで探していって、すべて配列に保存、その配列を逆順にして2^i*値で足していけばいける。
'''


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digit = []
        while head:
            digit.append(head.val)
            head = head.next
        digit.reverse()
        ans = 0
        for i in range(len(digit)):
            ans += 2**i*digit[i]
        print(ans)
        return ans
