# count-good-triplets.py
'''
制約的には愚直な O(N^3) 解法でも遅すぎるということはない。
ただ、それだけでいいのか?もっといい方法は?
'''


class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        length = len(arr)
        cnt = 0
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
        return cnt

    '''
    先に条件を計算してあげるとそれだけで相当計算速度が上がるっぽい。このアイデア賢い。
    ただネストが相当深くなるから、きれいに書ける方法があったらいいなぁ
    '''

    def countGoodTriplets2(self, arr, a: int, b: int, c: int) -> int:
        length = len(arr)
        cnt = 0
        for i in range(length):
            for j in range(i+1, length):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, length):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            cnt += 1
        return cnt


sol = Solution()
arr = [1, 1, 2, 2, 3]
a = 0
b = 0
c = 1
print(sol.countGoodTriplets2(arr, a, b, c))
