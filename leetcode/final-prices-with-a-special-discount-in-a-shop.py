# final-prices-with-a-special-discount-in-a-shop.py
class Solution:
    def finalPrices(self, prices):
        ans = []
        for i in range(len(prices)):
            price = prices[i]
            added = False
            for j in range(i+1,len(prices)):
                if price >= prices[j]:
                    ans.append(price-prices[j])
                    added = True
                    break
            if not added:
                ans.append(price)
        return ans

sol = Solution()
prices =[10,1,1,6]

print(sol.finalPrices(prices))
