# assign-cookies.py
from typing import List
import collections

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    ans += 1
                    s[j] = -1
                    break
        return ans

testcases = [
    [[1, 2, 3], [1, 1]],
    [[1, 2], [1, 2, 3]],
    [[1, 2, 3],[3]]
]
for g,s in testcases:
    sol = Solution().findContentChildren(g, s)
    print(sol)
