# squares-of-a-sorted-array.py
class Solution:
    def sortedSquares(self, A):
        ans = []
        for i in A:
            ans.append(i**2)
        return sorted(ans)


sol = Solution()
arr = [1, 2, 4]
print(sol.sortedSquares(arr))
