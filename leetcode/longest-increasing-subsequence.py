# longest-increasing-subsequence.py
'''
DP でやる感じだとは思うがどうやるかね…
解説ACしたけどこういうのホントキレイにかけてびっくりする…
そして O(nlogn) 解法があるらしい。
部分配列を構築していくイメージでソート済みのため二分探索で実装できるので logn に計算量を落とせる。
ただし、部分配列の長さは出すことができるが、構築する dp テーブルは実際の部分配列とならないのが注意。
(あくまで管理しているのは最長になる配列なので、前半に最長になる部分配列があり、
後半に前半より値の小さいが長さが足りない部分配列があると中身自体はおかしくなってしまう。
たとえば↓のサンプルだと中身はおかしくなる）
[10,20,30,40,50,2,3,4]
'''
class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1]*len(nums)
        length = len(nums)
        dp[0] = 1
        for i in range(1,length):
            for j in range(i):
                dp[i] = max(dp[j]+1, dp[i]) if nums[i] > nums[j] else dp[i]
            print(dp)
        return max(dp)

    def lengthOfLIS2(self, nums) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        len_dp = 1
        print(dp)
        for i in range(1, len(nums)):
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if dp[left] < nums[i]:
                dp.append(nums[i])
                len_dp += 1
            else:
                dp[left] = nums[i]
            print(dp)
        return len_dp


# nums = [10, 12, 13, 9, 2, 5, 3, 7, 9,101, 18]
nums = [10, 20, 30, 40, 50, 2, 3, 4]
# nums = [0, 1, 0, 3, 2, 3]
# sol = Solution().lengthOfLIS(nums)
sol = Solution().lengthOfLIS2(nums)
print(sol)
