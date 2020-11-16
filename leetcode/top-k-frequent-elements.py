# top-k-frequent-elements.py
'''
Python だったら counter で上位 N 個のものが出せるはず。
ただしそれだと面白くないのでどうするかと考えるのがよさそう。
> Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
となっているのでソートして個数をカウントするという方法は NG という感じ。
'''

import heapq


class Solution:
    # collencton.counter を自作で書き換え
    def counter(self, nums):
        ret = {}
        for i in nums:
            if not ret.get(i):
                ret[i] = 1
            else:
                ret[i] += 1
        return ret

    # heapq.nlargest を自作で書き換え
    def kFreakent(self, nums, k):
        pass

    def topKFrequent(self, nums, k: int):
        if k == len(nums):
            return nums
        counter = self.counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)


nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2

sol = Solution().topKFrequent(nums, k)
print(sol)
