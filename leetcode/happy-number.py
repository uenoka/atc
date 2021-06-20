# happy-number.py
'''
サイクル検出するだけでOK
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        tmp = 0
        seen = set()
        while tmp != 1:
            for c in n:
                tmp += int(c)**2
            if tmp == 1:
                return True
            if tmp in seen:
                return False
            seen.add(tmp)
            n = str(tmp)
            tmp = 0
        return True

testcases = [
    1,2,3,4,19
]
for n in testcases:
    sol = Solution().isHappy(n)
    print(sol)