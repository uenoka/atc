# abc130_b.py

N, X = map(int,input().split())
L = list(map(int,input().split()))
ans = 0
cnt = 1
for i in range(N):
    ans += L[i]
    if ans>X:
        break
    cnt+=1
print(cnt)