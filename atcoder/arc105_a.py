# arc105_a.py
a,b,c,d = map(int,input().split())
sums =sum((a,b,c,d))
if sums%2==1:
    print('No')
    exit()
for ai in range(2):
    for bi in range(2):
        for ci in range(2):
            for di in range(2):
                if ai*a+bi*b+ci*c+di*d == sums//2:
                    print('Yes')
                    exit()
print('No')