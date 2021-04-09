# check-if-n-and-its-double-exist.py
'''
ソートしてそれぞれの数で2倍の数があるかどうかを二分探索
-> hashMap を生成（それぞれの数が何個あるかを見る）してあげると線形で解ける
'''
class Solution:
    def binary_search(self,value,arr):
        left = 0
        right = len(arr)
        mid = (left + right)//2
        while right - left > 1:
            if arr[mid]==value:
                break
            if arr[mid] < value:
                left = mid
            if arr[mid] > value:
                right = mid
            mid = (left + right)//2
        return mid


    def checkIfExist(self, arr) -> bool:
        arr.sort()
        print(arr)
        for i,v in enumerate(arr):
            double_idx = self.binary_search(v*2, arr)
            # print(double_idx)
            if double_idx != i and arr[double_idx] == v*2:
                return True
        return False
testcases = [
    [10, 2, 5, 3],
    [7, 1, 14, 11],
    [3, 1, 7, 11],
    [-2, 0, 10, -19, 4, 6, -8],
    [0,0]
]
for arr in testcases:
    sol = Solution().checkIfExist(arr)
    print(sol)

