# peak-index-in-a-mountain-array.py
'''
線形解法
逐次比較して一度でも下降したらインデックスを返す

二分探索解法
ある位置の3要素を比較して、
・単調増加なら left = mid
・単調現象なら right = mid
・どちらでもなかったら真ん中の値がピーク

ちゃんと二分探索解法で1発で解けたのうれしいな。
'''


class Solution:
    def isIncrease(self, arr, mid):
        if arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
            return True
        return False

    def isDecrease(self, arr, mid):
        if arr[mid-1] > arr[mid] and arr[mid] > arr[mid+1]:
            return True
        return False

    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr)-1
        mid = len(arr)//2
        while left < right:
            if self.isIncrease(arr, mid):
                left = mid
            elif self.isDecrease(arr, mid):
                right = mid
            else:
                return mid
            mid = (left+right)//2
        return mid


sol = Solution()
# arr = [0, 10, 5, 2]
arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
# arr = [3, 4, 5, 1]
# arr = [0, 2, 1, 0]
# arr = [0, 1, 0]

print(sol.peakIndexInMountainArray(arr))
