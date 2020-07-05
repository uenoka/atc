# abc006_2.py
N = int(input())
ans = [-1]*(N+3)
ans[0]=0
ans[1]=0
ans[2]=1
for i in range(N-3):
    ans[i+3] =( ans[i]+ans[i+1]+ans[i+2])%10007
# print(ans)
print(ans[N-1])