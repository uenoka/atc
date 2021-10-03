N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in A:
    ans += max(0,i-K)
print(ans)
