# maximum-nesting-depth-of-the-parentheses.py
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
            if c == ')':
                stack.pop()
            if max_depth < len(stack):
                max_depth = len(stack)
        return max_depth


sol = Solution()
s = '(1)+((2))+(((3)))'
s = "1"
print(sol.maxDepth(s))
