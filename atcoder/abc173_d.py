# abc173_d.py
import math
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
for i in range(N-1):
    ans += A[math.ceil(i/2)]
print(ans)
