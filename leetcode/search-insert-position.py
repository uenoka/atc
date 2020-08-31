# search-insert-position.py
'''
愚直解法 → ソート済みなので下から見ていく
早い解法 → 二分探索
'''
import bisect


class Solution:
    '''
    二分探索
    '''

    def searchInsert(self, nums, target: int) -> int:
        return bisect.bisect_left(nums, target)

    '''
    愚直解法
    '''

    def searchInsert2(self, nums, target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return i+1


sol = Solution()
nums = [1, 3, 5, 6]
target = 2
print(sol.searchInsert(nums, target))
