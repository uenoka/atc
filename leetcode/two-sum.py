# two-sum.py
'''
丁度Googleのコーディングインタビューで出ていたものと同じ問題。
ただ、これうまく実装ができない…
'''


class Solution:
    def twoSum(self, nums, target):
        comp = {}
        for i, v in enumerate(nums):
            print(comp)
            if v in comp:
                return comp[v], i
            else:
                comp[target-v] = i
        return -1, -1


nums = [1, 2, 3, 4, 5, 6, 12, 13, 14, 15, 16, 7, 8, 9]
target = 18
# nums = [3, 3]
# target = 6
sol = Solution().twoSum(nums, target)
print(sol)
