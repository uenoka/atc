# coin-change.py
'''
DP の考え方（DPテーブル書いてどう動くか）はわかっているけど、自分で実装してできず解説AC。
にしてもLeetCodeのこの書き方きれいすぎてメモリ使用量も少なくてびっくりした。
'''

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x-coin]+1,dp[x])
            print(dp)
            print('========')
        return dp[amount] if dp[amount] != float('inf') else -1


sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins,amount))