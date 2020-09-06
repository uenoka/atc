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


sol = Solution()
mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

print(sol.diagonalSum(mat))
