# DPL_1_C.py
def printdp():
    for i in dp:
        print(i)
n, wmax = map(int,input().split())
V = [0]
W = [0]
for i in range(n):
    v,w = map(int,input().split())
    V.append(v)
    W.append(w)
dp =[ [0 for i in range(wmax+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,wmax+1):
        if j<W[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j] ,
                           dp[i-1][j-W[i]] + V[i] ,
                           dp[i][j-W[i]] + V[i])
print(dp[n][wmax])
