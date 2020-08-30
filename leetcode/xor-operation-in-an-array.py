# xor-operation-in-an-array.py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start+2*i
        return ans


sol = Solution()
n = 5
start = 0
print(sol.xorOperation(n, start))
