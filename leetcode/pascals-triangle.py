# pascals-triangle.py
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.pascals_triangle = [[1]*(i+1) for i in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,i):
                self.pascals_triangle[i][j] = self.pascals_triangle[i-1][j] + self.pascals_triangle[i-1][j-1]
        return self.pascals_triangle

testcases = [
    5
]
for numRows in testcases:
    sol = Solution().generate(numRows)
    print(sol)

