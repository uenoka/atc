# cells-with-odd-values-in-a-matrix.py
'''
最初対象の配列を作れという問題だと思ったからちょっと間違えた。
愚直にやらなくても何かしらいい解法がありそう。（結局奇数偶数を判断するだけだから、1回通るたびにT/F反転させて、最後にTrueをカウントするとか。）
とはいえこれでも↓くらいの結果にはなる。
Runtime: 52 ms, faster than 68.77% of Python3 online submissions for Cells with Odd Values in a Matrix.
Memory Usage: 13.9 MB, less than 49.52% of Python3 online submissions for Cells with Odd Values in a Matrix.

'''


class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        ans = [[0]*m for _ in range(n)]
        for row, col in indices:
            for i in range(len(ans[row])):
                ans[row][i] += 1
            for i in range(len(ans)):
                ans[i][col] += 1
        cnt = 0
        for i in ans:
            for j in i:
                if j % 2 == 1:
                    cnt += 1
        return cnt


n = 2
m = 3
indices = [[0, 1], [1, 1]]
sol = Solution()
print(sol.oddCells(n, m, indices))
