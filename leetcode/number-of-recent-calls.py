# number-of-recent-calls
'''
こういう問題競プロにはないから勉強になる。クラスを作ってみる系の問題もっとトライしてみたい。
こういう系の専用のリスト作っておこう。
'''


import collections


class RecentCounter:

    def __init__(self):
        self.recent_ping = collections.deque()

    def ping(self, t: int) -> int:
        self.recent_ping.append(t)
        while self.recent_ping[0] < t-3000:
            self.recent_ping.popleft()
        return len(self.recent_ping)

    def toString(self):
        return self.recent_ping


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
print(param_1)
print(obj.toString())

param_1 = obj.ping(2)
print(param_1)
print(obj.toString())

param_1 = obj.ping(3001)
print(param_1)
print(obj.toString())

param_1 = obj.ping(3002)
print(param_1)
print(obj.toString())
