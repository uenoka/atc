# abc129_b.py
N = int(input())
W = list(map(int,input().split()))
ans = 10**10
for i in range(N):
    _sum = abs(sum(W[:i])-sum(W[i:]))
    if ans >= _sum:
        ans = _sum
print(ans)