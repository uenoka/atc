# lucky-numbers-in-a-matrix.py
'''
解けはしたが、何となく正当性が微妙…これはもう少し置いてから再挑戦したほうがよさそう
'''


class Solution:
    def luckyNumbers(self, matrix):
        maxcol = [-1000000]*len(matrix[0])
        minrow = []
        for row in matrix:
            minrow.append(min(row))
            for i, col in enumerate(row):
                if col > maxcol[i]:
                    maxcol[i] = col
        print(minrow, maxcol)
        ans = []
        for i in minrow:
            for j in maxcol:
                if i == j:
                    ans.append(j)
        return ans


sol = Solution()

# matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix = [[7, 8], [1, 2]]
# matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(sol.luckyNumbers(matrix))
