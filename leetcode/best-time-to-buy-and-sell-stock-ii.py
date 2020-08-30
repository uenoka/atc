# best-time-to-buy-and-sell-stock-ii.py
'''
利益を最大化するには下がる瞬間に売る=単調非減少であれば差を入れるだけでよい。
ただこれ下位17%なので、もう少しいい解法がありそう。O(N)のはずなんだけどな。。。
'''


class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                ans += prices[i+1]-prices[i]
        return ans


sol = Solution()
prices = [1, 2, 3, 4, 5]
print(sol.maxProfit(prices))
