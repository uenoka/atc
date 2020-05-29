# abc083_b.py
N,A,B = map(int,input().split())
ans = 0
for i in range(N+1):
    s = str(i)
    add = 0
    for j in s:
        add += int(j)
    if add <= B and add>= A:
        ans += i
print(ans)