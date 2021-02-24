# house-robber-ii.py
'''
動的計画法かなー？
'''

class Solution:
    def rob(self, nums) -> int:
        return 0

test_cases = [
    [0],
    [2, 3, 2],
    [2, 1, 3, 1, 4, 1, 1, 100, 1, 1],
    [1, 2, 3, 1]
]

for nums in test_cases:
    sol = Solution().rob(nums)
    print(sol)
