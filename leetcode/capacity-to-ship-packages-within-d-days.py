# capacity-to-ship-packages-within-d-days.py
'''
案1 : 二分探索で境界値を求めて毎回シミュレーション O(NlogN)
最大値はどこ？ → 1日で届ける必要がある場合もあるので 500 * 5*10^4 = 25 * 10^6
'''
class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        right = 25 * 10**6
        left = max(weights)
        mid = (right + left )//2
        while right - left > 1:
            # print('=============')
            # print('left,mid,right',left,mid,right)
            if self.can_ship(weights, D, mid):
                right = mid
                mid = (right + left )//2
            else:
                left = mid
                mid = (right + left )//2
        return left
    def can_ship(self, weights, D, mid):
        cnt = 1
        tmp_weight = 0
        # print(mid)
        for weight in weights:
            if mid < weight:
                return False
            if mid > tmp_weight + weight:
                tmp_weight+= weight
            else:
                # print(mid,tmp_weight)
                tmp_weight =weight
                cnt += 1
        # print('mid is',mid,' cnt is ',cnt," D is ",D,cnt <= D)
        return cnt <= D

sol = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
# weights = [3,2,2,4,1,4]
# D = 3
# weights = [1,2,3,1,1]
# D = 4
print('ans is ',sol.shipWithinDays(weights,D))