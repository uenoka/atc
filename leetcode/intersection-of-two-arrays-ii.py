# intersection-of-two-arrays-ii.py
'''
そんなむずくはないけど結構問題文の意図を読み取るのが難しかった。
'''
from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums2 = collections.Counter(nums2)
        for num in nums1:
            if num in nums2.keys() and nums2[num] > 0:
                nums2[num] -= 1
                ans.append(num)
        return ans

testcases = [
    [[1, 2, 2, 1], [2, 2]],
    [[1, 2, 2, 1], [1, 2, 2]],
    [[4, 9, 5], [9, 4, 9, 8, 4]],
]
for nums1,nums2 in testcases:
    sol = Solution().intersect(nums1,nums2)
    print(sol)
