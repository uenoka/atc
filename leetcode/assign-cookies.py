# assign-cookies.py
'''
愚直に全探索で実装。
two pointers で O(N) に計算量削減ができる
'''
from typing import List

class Solution:
    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        gidx = 0
        sidx = 0
        while gidx < len(g) and sidx < len(s):
            if g[gidx] <= s[sidx]:
                ans += 1
                gidx += 1
                sidx += 1
            else:
                sidx += 1

        return ans

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
    sol = Solution().findContentChildren2(g, s)
    print(sol)
