# matrix-diagonal-sum.py


class Solution:
    def diagonalSum(self, mat) -> int:
        left = 0
        right = len(mat[0])-1
        idx = 0
        ans = 0
        mid = len(mat)//2
        while right >= 0 and left < len(mat[0]):
            while idx < len(mat):
                ans += mat[idx][left]
                ans += mat[idx][right]
                idx += 1
                left += 1
                right -= 1
        if len(mat) % 2 == 1 and len(mat[0]) % 2 == 1:
            ans -= mat[mid][mid]
        return ans


'''
ちょっと while 2重なのが（計算量は本質的には変わらないはずだけど）邪魔だから1重にしてみた。
速度は 33% faster なのでほぼ変わらず。多分 O(N) でそういう表示になるっぽいなぁ、あとはPythonの書き方で早くなるかどうかとか検証する感じなのかな？
'''


def diagonalSum2(self, mat) -> int:
    idx = 0
    mid = len(mat)//2
     length = len(mat)-1
      ans = 0
       for i in mat:
            ans += i[idx] + i[length-idx]
            idx += 1
        if length % 2 == 0 and length % 2 == 0:
            ans -= mat[mid][mid]
        return ans


sol = Solution()
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(sol.diagonalSum2(mat))
