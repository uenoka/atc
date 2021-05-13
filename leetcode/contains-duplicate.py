# contains-duplicate.py
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
testcases = [
    [1,2,3,4,5]
    ,[1,1,2,3,4,5]
    ,[1,2,3,4,5,1]
]
for nums in testcases:
    sol = Solution().containsDuplicate(nums)
    print(sol)