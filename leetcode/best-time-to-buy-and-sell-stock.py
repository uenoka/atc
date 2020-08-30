# best-time-to-buy-and-sell-stock.py
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices) -> int:
        minv = 10**4+1
        maxv = 0
        for i in prices:
            maxv = max(maxv, i-minv)
            minv = min(i, minv)
        return maxv


sol = Solution()
prices = [6, 5, 4, 4, 1]
print(sol.maxProfit(prices))
