# find-k-pairs-with-smallest-sums.py
'''
nums1,2 の長さを N, M とすると愚直解ではO(NMlogNM)
改善点1：まずはk個までしか必要ない=ループはk個ずつで十分
'''
import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        ans = []
        for i in range(k):
            for j in range(k):
                if i < len(nums1) and j < len(nums2):
                    ans.append([nums1[i], nums2[j]])
        return heapq.nsmallest(k, ans, key=lambda x: sum(x))


# nums1 = [1, 7, 11]
# nums2 = [2, 4, 6]
# k = 3
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2

sol = Solution().kSmallestPairs(nums1, nums2, k)
print(sol)
