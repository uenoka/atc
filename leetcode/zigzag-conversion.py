# zigzag-conversion.py
'''
1 往復が numRows*2-2 周期だからそれをうまく使って、と思ったがうまくできず。
Solution みたらめっちゃわかりやすくてビビった。
最初に isReverse を True で初期化しておくことで、最初の文字に入るときに isReverse = not isReverse になるので正の方向に進む、
numRows-1 まで来たらひっくり返すとするだけでめちゃくちゃきれいに書ける。
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        col = [""]*numRows
        isReverse = True
        currentRow = 0
        for c in s:
            col[currentRow] += c
            if currentRow == 0 or currentRow == numRows-1:
                isReverse = not isReverse
            currentRow = currentRow + 1 if isReverse else currentRow - 1
        ans = ""
        for subs in col:
            ans += subs
        return ans

testcases = [
    ("AB",1)
]
for s,numRows in testcases:
    sol = Solution().convert(s,numRows)
    print(sol)
