# can-make-arithmetic-progression-from-sequence.py

'''
配列の要素を適宜並べ替えて、 A[i], A[i+1] の差が同じになるかどうかを判定する。
ソートして差をとっていく→1つでも異なればFalseでいける。
'''


class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        diff = arr[0]-arr[1]
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i+1] != diff:
                return False
        return True


sol = Solution()
arr = [1, 2, 4]
print(sol.canMakeArithmeticProgression(arr))
