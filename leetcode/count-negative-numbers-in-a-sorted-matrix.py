# count-negative-numbers-in-a-sorted-matrix.py
class Solution:
    def countNegatives(self, grid) -> int:
        ans = 0
        for row in grid:
            for col in row:
                if col <0:
                    ans+=1
        return ans

sol = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(grid))
