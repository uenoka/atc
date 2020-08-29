# abc176_c.py
N = int(input())
A = list(map(int,input().split()))
m = 0
ans = 0
for i in A:
    if m < i:
        m = i
    ans += max(0,m-i)
print(ans)