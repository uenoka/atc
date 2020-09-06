# height-checker.py
'''
愚直に考えるとソートして要素比較する感じだが、他にいい方法がある…?
'''


class Solution:
    def heightChecker(self, heights) -> int:
        s = sorted(heights)
        ans = 0
        for i in range(len(s)):
            if s[i] != heights[i]:
                ans += 1
        return ans


sol = Solution()
arr = [1, 1, 4, 2, 1, 3]

print(sol.heightChecker(arr))
