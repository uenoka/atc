# 20200612_yorukatsu_a.py
N, A, B = map(int,input().split())
ans = 0
for i in range(N+1):
    tmp = str(i)
    _sum = 0
    for j in tmp:
        c=int(j)
        _sum+=c
    if _sum >=A and _sum <=B:
        ans += i
print(ans)