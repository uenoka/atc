# excel-sheet-column-number.py
class Solution:
    def __init__(self):
        self.alphabet = {c : i+1 for i,c in enumerate('abcdefghijklmnopqrstuvwxyz'.upper())}
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = reversed(columnTitle)
        ans = 0
        for i,c in enumerate(columnTitle):
            # print(i,c)
            ans += 26**i*self.alphabet[c]
        return ans

testcases = [
    "A",
    "AB",
    "ZY",
    "FXSHRXW"
]
for columnTitle in testcases:
    sol = Solution().titleToNumber(columnTitle)
    print(sol)
