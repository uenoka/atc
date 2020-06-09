# arc073_a.py
N, T = map(int,input().split())
t = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    ans += min(t[i+1]-t[i],T)
ans += T
print(ans)
