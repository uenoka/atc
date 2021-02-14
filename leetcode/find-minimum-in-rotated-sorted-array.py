'''
流石に min(nums) じゃつまらないので他の解法を探す…
昇順に並んでいた配列内の要素が右にいくつかシフトしたものが与えられる。
その中の最小値を取得して返せ。
例：
input : [4,5,6,1,2,3]
output: 1
制約：
配列の長さは5000まで、値は -5000~5000 まで
二分探索でやるにはちょっと重厚すぎる実装な気はする。。。（これが制約なら普通に全探索で変曲点見つければよさそう）
'''

class Solution:
    def findMinWithMinFunction(self, nums) -> int:
        return min(nums)

    def findMin(self, nums) -> int:
        left = 0
        right = len(nums)-1
        if nums[left]<=nums[right]:
            return nums[left]
        mid = (left + right)//2
        print(left, mid, right)
        while mid - left > 1 or right-mid > 1:
            if nums[left] > nums[mid]:
                right = mid
                mid = (left + right)//2
            else:
                left = mid
                mid = (left + right)//2
        print(left,mid,right)
        return nums[mid] if nums[mid-1] > nums[mid] else nums[mid+1]


nums = [2, 3, 4, 5, 6, 1]
sol = Solution().findMin(nums)
print(sol)
