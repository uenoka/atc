# median-of-two-sorted-arrays.py
'''
これで通りはする、ただし求められた計算量にはできていないって感じ。
今回の計算量は O((N+M)log(N+M))
求められているのは O(log(N+M))
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        nums = nums1+nums2
        nums.sort()
        if (n+m) % 2 == 0:
            return (nums[(n+m)//2]+nums[(n+m)//2-1])/2
        else:
            return nums[(n+m)//2]
