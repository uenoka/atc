# min-cost-climbing-stairs.py
'''
基本的な DP で練習問題に丁度いい（flogの問題を、高さの計算をせずに与えられたものとして考える感じ。）
'''


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0]*(len(cost)+1)  # Dp テーブルを「その階段に到達するときの最小のコスト」として考える
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
            # print(dp)
        return dp[-1]


sol = Solution()
# cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(sol.minCostClimbingStairs(cost))
