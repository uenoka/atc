# abc099_c.py
'''
6**6 = 46656
9**5 = 59049
がそれぞれ100000を超えない最大の値なのでテーブルをこれと1でもっておいてDPしてあげる
メモリをより少なくしたければ1, 6, 9 だけにして、6,9の累乗にあたった時には1を記入するようにするとよい
解けそうなのに解けない…
'''


def printdp():
    for i in dp:
        print(i)


N = int(input())
m = 100000
inf = 10**9+7
dp = [inf]*(N+1)

# printdp()
dp[0] = 0
for i in range(1, N+1):
    pow6 = 1
    pow9 = 1
    while pow6 <= i:
        dp[i] = min(dp[i], dp[i-pow6]+1)
        pow6 *= 6
    while pow9 <= i:
        dp[i] = min(dp[i], dp[i-pow9]+1)
        pow9 *= 9
print(dp)
print(dp[N])
