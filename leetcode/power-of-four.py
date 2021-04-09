# power-of-four.py
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n/4)


testcases = [
    27,
    3,
    1,
    21,
    45,
    9,
    0,
    -1,
    -9,
    -27,
    4,
    16,
    64
]
for n in testcases:
    sol = Solution().isPowerOfFour(n)
    print(sol)
