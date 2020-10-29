# dp_d.py
N, W = map(int,input().split())
V = []
for i in range(N):
    v = list(map(int,input().split()))
    V.append(v)
dp =  [0]*(W+1)
dp[0] = 0
for i in range(1,W+1):
    for wv in V:
        _max = []
        if i + wv[0]<W:
            _max.append(dp[i]+wv[1])
        if _max:
            dp[i+wv[0]]=max(_max)
print(dp)