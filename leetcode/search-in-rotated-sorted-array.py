# search-in-rotated-sorted-array.py
'''
二分探索でいくべきなのはわかるが、Python だと1行で高速にできてしまうからなぁ…
'''
class Solution:
    def search(self, nums, target: int) -> int:
        return nums.index(target) if target in nums else -1

testcases = [
    ([4, 5, 6, 7, 0, 1, 2],0),
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([1], 0)
]

for nums,target in testcases:
    sol = Solution().search(nums,target)
    print(sol)
