# toeplitz-matrix.py
class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        pre = matrix[0][:-1]
        for row in range(1, len(matrix)):
            if not pre == matrix[row][1:]:
                return False
            pre = matrix[row][:-1]
        return True


matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
sol = Solution()
print(sol.isToeplitzMatrix(matrix))
