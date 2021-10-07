# ugly-number.py

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:return False
        divs = [2,3,5]
        for d in divs:
            while n%d == 0:
                n//= d
        return n == 1

testcases =[
    905391974,
    0,
    -6,
    14, # false
    15,
    18,
    120
]
for n in testcases:
    sol = Solution().isUgly(n)
    print(sol)
