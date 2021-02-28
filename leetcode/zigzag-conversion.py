# zigzag-conversion.py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        col = [""]*numRows
        counter = 2*numRows - 2
        for i,c in enumerate(s):
            print()

        return ""

testcases = [
    ("PAYPALISHIRING", 3), ("PAYPALISHIRING",4), ("A", 1)
]
for s,numRows in testcases:
    sol = Solution().convert(s,numRows)
    print(sol)
