# remove-outermost-parentheses.py
'''
整合性を保ちながらカッコの一番外側を外す問題。
例 :
(()()())(()()) -> ()()()()()
()(()(()))((())()) -> ()()(())(())()
stack でカッコを管理して、空以外の時には新しい配列にカッコを入れてあげればよい。
'''


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        ans = []
        for p in S:
            if not stack:
                stack.append(p)
            elif p == ")":
                stack.pop()
                if stack:
                    ans.append(p)
            else:
                stack.append(p)
                ans.append(p)
        return "".join(ans)


sol = Solution()
S = "(()())(())(()(()))"
print(sol.removeOuterParentheses(S))
