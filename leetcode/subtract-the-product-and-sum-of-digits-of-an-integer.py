# subtract-the-product-and-sum-of-digits-of-an-integer.py
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sums = 0
        mults = 1
        for i in n:
            v = int(i)
            sums += v
            mults *= v
        return mults - sums


sol = Solution()
n = 234
print(sol.subtractProductAndSum(n))
