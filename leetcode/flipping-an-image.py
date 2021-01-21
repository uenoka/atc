# flipping-an-image.py
class Solution:
    def flipAndInvertImage(self, A):
        ans = [[0]*len(A[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                ans[i][len(A[i])-j-1] = 1 if A[i][j]==0 else 0
        return ans


sol = Solution()
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(sol.flipAndInvertImage(A))
