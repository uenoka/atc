# power-of-three.py
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n/3)

testcases = [
    27,
    3,
    1,
    21,
    45,
    9,
    0,
    - 1,
    - 9,
    - 27,
]
for n in testcases:
    sol = Solution().isPowerOfThree(n)
    print(sol)