# majority-element.py
'''
counter の most common が一番わかりやすいからこれで。
max(counts.keys(), key=counts.get) でも行けるらしい。 key=counts.get のところが何してるのかよくわからないな…
'''

import collections


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums) -> int:
        C = collections.Counter(nums)
        return C.most_common(1)[0][0]


sol = Solution()
nums = [1, 1, 1, 2, 3, 2, 4, 5]
print(sol.majorityElement(nums))
