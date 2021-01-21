# array-partition-i.py

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                ans += v
        return ans


    '''
    Python だとこういう書き方ができるのもうちょっと勉強したほうがいいな
    '''
    def arrayPairSum2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


sol = Solution()
arr = [1, 4, 3, 2]
print(sol.arrayPairSum(arr))
