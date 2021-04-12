# find-the-highest-altitude.py
class Solution:
    def largestAltitude(self, gain) -> int:
        m = 0
        cumsum = 0
        for i in gain:
            cumsum += i
            m = max(cumsum,m)
        return m

testcases = [
    [-5, 1, 5, 0, -7],
    [-4, -3, -2, -1, 4, 3, 2]
]
for gain in testcases:
    sol = Solution().largestAltitude(gain)
    print(sol)




