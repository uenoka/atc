# DPL_1_A.py
def printdp():
    for row in dp:
        for i in row:
            print(i if i!=10**9 else "00",end=",")
        print()
N, M = map(int, input().split())
C = [0]
C += list(map(int, input().split()))
dp = [[10**9 for i in range(N+1)] for i in range(M+1)]
dp[1][0]=0
for i in range(1, M+1):
    for j in range(N+1):
        if j==0:
            dp[i][j]=0
        elif j < C[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-C[i]]+1) 
        #     print("i,j:",i,j,", dp[i-1][j], dp[i][j-C[i]+1]+1",dp[i-1][j], dp[i][j-C[i]+1]+1)
        # print(dp[i][j])
# printdp()
print(dp[M][N])
