# water-bottles.py

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        while numBottles >= 1:
            print(numBottles)
            ans += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
        return ans


sol = Solution()
numBottles = 9
numExchange = 3

print(sol.numWaterBottles(numBottles, numExchange))
