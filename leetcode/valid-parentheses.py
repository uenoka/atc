# valid-parentheses.py
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if stack:
                    # print(parentheses.get(c))
                    if stack.pop() != parentheses.get(c):
                        return False
                else:
                    return False
            # print(stack)
        if stack:
            return False
        return True


# s = "()[]{}"
s = '{[]()[[]]}'
# s = "(]"
sol = Solution().isValid(s)
print(sol)
