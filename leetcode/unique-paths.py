# unique-paths.py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)


sol = Solution()
m=3
n=2
m = 3
n = 7
print(sol.uniquePaths(m,n))