# kth-largest-element-in-a-stream.py
'''
単純に実装しようと思うと毎回ソートしたりして無駄が多そう。
どういうデータの持ち方をすれば効率がいいかを考える
→ 優先度付きキューを使用するらしい。
heapq 要学習
heapq は優先度付きキューの実装の1つ。
大きい順（小さい順）に優先度があるというような形で保持できるらしい。（本当かどうかは要確認）
そのうえで ↓ の実装は K 番目までの大きさのもののみを保持しておいて、大きいものが来たら入れ替えを行う、小さいものが来たら無視する、返す値はnums[0](上位Kのうち最小の値)
確かにこれならほかの小さい値は無視すればいいし頭がいいなー。
'''

import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]


k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
params = [3, 5, 10, 9, 4]
for param in params:
    print(obj.add(param))
