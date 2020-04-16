# abc118_b.py
N, M = map(int,input().split())
A = []
ans_list = [0]*(M+1)
ans = 0
for i in range(N):
    _,*a = list(map(int,input().split()))
    A.append(a)
for i in A:
    for j in i:
        ans_list[j] += 1
for i in ans_list[1:]:
    if i == N:
        ans += 1
print(ans)