# decompress-run-length-encoded-list.py
'''
ランレングス圧縮がどいう言うものかという知識と一緒に学べてよい問題。
'''


class Solution:
    def decompressRLElist(self, nums):
        ans = []
        for i in range(len(nums)//2):
            counter = nums[i*2]
            val = nums[i*2+1]
            for i in range(counter):
                ans.append(val)
        return ans


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.decompressRLElist(nums))
