# minimum-path-sum.py
'''
グリッドグラフ上での最短コスト→ダイクストラでよさそう
→もっと単純にGrid最短経路のDPでよさそう
'''
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==1:
            return sum(grid[0])
        dp = [[float("INF")]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        cumsum = 0
        for i in range(len(grid[0])):
            cumsum += grid[0][i]
            dp[1][i+1] = cumsum
        for i in range(2,len(grid)+1):
            dp[i-1][0] = 0
            for j in range(1,len(grid[0])+1):
                dp[i][j] = min(dp[i][j-1]+grid[i-1][j-1],dp[i-1][j]+grid[i-1][j-1])
        return dp[len(grid)][len(grid[0])]

testcases = [
    [[1,3,1],[1,5,1],[4,2,1]],
    [[1,2,3],[4,5,6]],
    [[0]],
    [[1,2],[1,1]]
]
for grid in testcases:
    sol = Solution().minPathSum(grid)
    print(sol)