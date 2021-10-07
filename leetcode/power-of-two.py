# power-of-two.py
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n%2==0:
            n//=2
        return n==1


testcases = [
    905391974,
    0,
    -6,
    14,  # false
    15,
    18,
    120
]
for n in testcases:
    sol = Solution().isPowerOfTwo(n)
    print(sol)
