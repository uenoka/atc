# dp_c.py
N = int(input())
A=[]
for i in range(N):
    a= list(map(int,input().split()))
    A.append(a)
dp=[[] for i in range(N)]
dp[0]=A[0]

for i in range(1,N):
    ai = max(dp[i-1][1],dp[i-1][2]) + A[i][0]
    bi = max(dp[i-1][0],dp[i-1][2]) + A[i][1]
    ci = max(dp[i-1][1],dp[i-1][0]) + A[i][2]
    dp[i]=[ai,bi,ci]
print(max(dp[N-1]))