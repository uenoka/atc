# excel-sheet-column-number.py
class Solution:
    def __init__(self):
        self.alphabet = {i+1:c for i,c in enumerate('abcdefghijklmnopqrstuvwxyz'.upper())}

    def convertToTitle(self, columnNumber: int) -> str:
        divider = 26
        ans = ''
        while columnNumber > 0:
            charIdx = columnNumber % divider
            columnNumber = columnNumber // divider
            if charIdx == 0:
                columnNumber -= 1
                charIdx = divider
            ans = self.alphabet[charIdx] + ans
            print(ans)
        return ans

testcases = [
    1,
    26,
    27,
    701,
    2**31-1
]

for columnNumber in testcases:
    print('===start===')
    sol = Solution().convertToTitle(columnNumber)
    print('ans is ' + sol)


