# find-the-duplicate-number.py
'''
ソートして重複を見つける→time O(logN), space O(1)
setに既存の値を入れていく → time O(N), space O(N)
2重ループ → time O(N^2), space O(1)
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
Cycle detection (Floyd's Tortoise and Hare) という解法もあるらしい（Linked listのサイクル検知と同じような方法?）
'''
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

testcases = [
    [1,1],
    [1,1,2],
    [1,3,4,2,2],
    [3,1,3,4,2]
]
for nums in testcases:
    sol = Solution().findDuplicate(nums)
    print(sol)
