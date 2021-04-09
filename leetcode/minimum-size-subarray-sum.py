# minimum-size-subarray-sum.py
'''
累積和で実装できそうな気がする。
ただし、最小値を求めるので結局全部見に行かないといけないが、制約が N <= 10^5 なのでO(N^2) では間に合わない
-> 二分探索で NlogN 落としてみる.
どうにか実装できたけどこれ結構な厳しさがあったな…めちゃくちゃ汚い…
別解で尺取り法がある（こっちだと O(N) なのでこっちのほうが良い。）
'''
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        cumsum = [0]
        tmpsum = 0
        for i in nums:
            tmpsum += i
            cumsum.append(tmpsum)
        print(cumsum)
        return self.minSubArrayLenBinarySearch(s, cumsum)
        # return self.minSubArrayLenTwoPointer(s, cumsum)

    def minSubArrayLenTwoPointer(self, s: int, cumsum) -> int:
        return 0

    def minSubArrayLenBinarySearch(self, s: int, cumsum) -> int:
        if cumsum[-1] < s:
            return 0
        if cumsum[1] >= s:
            return 1
        min = len(cumsum)-1
        for i in range(2,len(cumsum)):
            left = 1
            right = i
            mid = (left + right)//2
            # print(left,mid,right)
            while right > mid and mid > left:
                # print(left, mid, right, 'cumsum[right]-cumsum[mid-1] : ', cumsum[right]-cumsum[mid-1])
                if cumsum[right]-cumsum[mid]>=s:
                    if min > right - mid:
                        min = right - mid
                    left = mid
                    mid = (left + right)//2
                else:
                    mid=(left+mid)//2
            if cumsum[right]-cumsum[mid-1] >= s:
                if min > right - mid:
                    min = right - mid + 1

            # print('min is ',min)
        return min


testcases = [
    (7, [2, 3, 1, 2, 4, 3]),
    (4, [1, 4, 4]),
    (11, [1, 1, 1, 1, 1, 1, 1, 1, 1]),
    (11,[1, 2, 3, 4, 5]),
    (15,[1, 2, 3, 4, 5]),
    (5,[2, 3, 1, 1, 1, 1, 1])
]

for s, nums in testcases:
    sol = Solution().minSubArrayLen(s,nums)
    print(sol)
