# split-a-string-in-balanced-strings.py
'''
stack で管理するとやりやすい。
↓の問題の類題とも言えそう。
https://leetcode.com/problems/valid-parentheses/
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        cnt = 0
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] == c:
                stack.append(c)
            else:
                stack.pop()
            if not stack:
                cnt += 1
        return cnt


sol = Solution()
s = 'RLRRRLLRLL'
print(sol.balancedStringSplit(s))
