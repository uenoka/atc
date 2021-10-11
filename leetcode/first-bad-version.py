# first-bad-version.py

class Solution:
    def __init__(self,n):
        self.badversion = n
    def isBadVersion(self,n):
        return self.badversion <= n

    def firstBadVersion(self, n):
        left = 0
        right = n + 1
        mid = (left + right)//2
        print(left,right)
        while left < right-1:
            print(left, right)
            if self.isBadVersion(mid):
                right = mid
                mid = (left + right)//2
            else:
                left = mid
                mid = (left + right)//2
        return right
testcases = [1,2,3,4,5,1000]
import random
for n in testcases:
    badversion = random.randint(1, n)
    print("badversion", badversion)
    sol = Solution(badversion)
    print(sol.firstBadVersion(n))
