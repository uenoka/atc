# unique-paths-ii.py
'''
この問題は安心感がある…
M*N グリッド上にものがあったら通れない状況で何パターンのゴールへの行き方があるか。
動的計画法でものがある場所は 0 、それ以外は足していくという感じでいくとよい。
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid[0]), len(obstacleGrid)
        print(m,n)
        dp = [[0]*m for _ in range(n)]
        return dp


testcases = [
    [[0, 1], [0, 0], [0, 0]],
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
]
for obstacleGrid in testcases:
    sol = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(sol)
