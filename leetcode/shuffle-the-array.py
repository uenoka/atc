class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i+n])
        return ret


sol = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(sol.shuffle(nums, n))
