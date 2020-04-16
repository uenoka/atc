# abc096_b.py
A = list(map(int,input().split()))
A.sort(reverse=True)
N = int(input())
ans = 0
for i,v in enumerate(A):
    if i == 0:
        ans += v*(2**N)
    else:
        ans += v
print(ans)