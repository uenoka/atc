# zigzag-conversion.py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        col = [""]*numRows
        counter = 0
        for i,c in enumerate(s):
            col[i]

        return ""

testcases = [
    ("PAYPALISHIRING", 3), ("PAYPALISHIRING",4), ("A", 1)
]
for s,numRows in testcases:
    sol = Solution().convert(s,numRows)
    print(sol)