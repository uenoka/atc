# abc092_b.py
import math
N = int(input())
D, X = map(int,input().split())
A = [int(input()) for i in range(N)]
ans = X
for i in A:
    ans += math.ceil(D/i)
print(ans)

