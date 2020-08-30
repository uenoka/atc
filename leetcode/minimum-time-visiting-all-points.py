# minimum-time-visiting-all-points.py
class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        length = len(points)
        ans = 0
        for i in range(length-1):
            ans += max(abs(points[i][0]-points[i+1][0]),
                       abs(points[i][1]-points[i+1][1]))
        return ans


sol = Solution()
points = [[3, 2], [-2, 2]]
print(sol.minTimeToVisitAllPoints(points))
