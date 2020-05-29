# agc027_a.py
n,x = map(int,input().split())
a = list(map(int,input().split()))
if sum(a) == x:
    print(n)
    exit()

a.sort()
cnt = 0
for i in a:
    if x>=i:
        cnt += 1
        x -= i
if cnt == n:
    cnt-=1
print(cnt)
