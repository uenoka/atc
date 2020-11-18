# subarray-sum-equals-k.py
'''
しゃくとり法 (two pointers / sliding window) で実装する。
→違った。ちゃんとHashMapだった。
けど動きがわからん…
'''


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cnt = 0
        sum = 0
        maps = {}
        maps[0] = 1
        for i in nums:
            sum += i
            if maps.get(sum-k):
                cnt += maps.get(sum-k)
            maps[sum] = (0 if not maps.get(sum) else maps.get(sum))+1
        return cnt


# nums = [1, 1, 1]
# k = 2
nums = [1, 2, 3]
k = 3
# nums = [1]
# k = 0
# nums = [-1, -1, 1]
# k = 0

sol = Solution().subarraySum(nums, k)
print(sol)
