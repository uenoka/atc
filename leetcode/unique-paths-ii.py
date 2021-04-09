# unique-paths-ii.py
'''
この問題は安心感がある…
M*N グリッド上にものがあったら通れない状況で何パターンのゴールへの行き方があるか。
動的計画法でものがある場所は 0 、それ以外は足していくという感じでいくとよい。
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        c,r = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0]*(c+1) for _ in range(r+1)]
        dp[1][1] = 1
        seen = set()
        seen.add((1,1))
        for i in range(1,r+1):
            for j in range(1,c+1):
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j] = 0
                elif (i,j) not in seen:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                    seen.add((i,j))
        return dp[r][c]


testcases = [
    [[0, 1], [0, 0], [0, 0]],
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]],   

]
for obstacleGrid in testcases:
    sol = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(sol)
