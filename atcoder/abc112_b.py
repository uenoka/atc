# abc112_b.py
N, T = map(int,input().split())
C = [map(int,input().split()) for i in range(N)]
ans = 10001
for c,t in C:
    if t <= T and ans > c:
        ans = c
if ans <1001:
    print(ans)
else:
    print("TLE")