# missing-number.py
'''
O(1) で1~N までの和を求められるので、総和から各桁の値を引いていけば良い
sum のほうが早い？？
'''
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        ans = (length**2+length)//2
        return ans - sum(nums)
testcases = [
    [0,1,2,3,4,5],
    [0,1,2,3,5],
]
for nums in testcases:
    sol = Solution().missingNumber(nums)
    print(sol)