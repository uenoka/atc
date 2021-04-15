# sqrtx.py
'''
いろんな方法があると思うからそれぞれ実装してみる
・普通に int(x**0.5)
・二分探索で対象をみつける（2乗してxを超えない最大の数を見つける）
やっぱりちゃんと数値計算でやると速い（それぞれ 28 ms, 48 ms）
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        def sq1(x):
            return int(x**0.5)
        def sq2(x):
            if x <= 1:
                return x
            left = 0
            right = x
            mid = right//2
            while right - left > 1:
                if mid**2 == x:
                    return mid
                elif mid**2 > x:
                    right = mid
                else:
                    left = mid
                mid = (right + left) //2 
            return left
        return sq2(x)

testcases =[
    1,2,3,4,5,6,7,8,9
]
for x in testcases:
    sol = Solution().mySqrt(x)
    print(sol)
