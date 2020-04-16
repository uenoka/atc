# agc014_a.py]
A, B, C = map(int,input().split())
cnt = 0
inf = 15
for i in range(inf):
    if A%2==0 and B%2==0 and C%2==0: 
        a = (B+C)//2
        b = (A+C)//2
        c = (B+A)//2
        A = a
        B = b
        C = c
        cnt += 1
    else:
        break
if cnt == inf:
    cnt = -1
print(cnt)