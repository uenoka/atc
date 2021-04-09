# paiza_a035.py
'''
これで通らないのなんでや…
'''
M = int(input())
A = [0]
A += [int(input()) for i in range(M)]
A.sort()
dp = [[0]*101 for i in range(M+1)]
dp[0][0]=1
for i in range(1,M+1):
    for j in range(101):
        if A[i]<=j:
            dp[i][j] = 0 if dp[i-1][j-A[i]]== 0 else 1
        else:
            dp[i][j] = dp[i-1][j]

ans = 0
point = []
for i in range(101):
    if dp[M][i] != 0:
        point.append(i)
        ans +=1
print(ans)
for i in point:
    print(i)