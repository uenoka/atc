# paiza_a035.py
import itertools
N = int(input())
A = [int(input()) for i in range(N)]

dp = [False]*101
dp[0] = True
used = [[] for i in range(101)]
for i in range(101):
    for point in A:
        if A.count(point) == 1:
            if i + point < 101 and dp[i] and used[i].count(point) < 1:
                used[i].append(point)
                used[i+point].append(point)
                dp[i + point] = True
        else:
            if i + point < 101 and dp[i] and used[i].count(point) <= A.count(point):
                used[i].append(point)
                used[i+point].append(point)
                dp[i + point] = True

print(dp.count(True))
for i, flg in enumerate(dp):
    if flg:
        print(i)
