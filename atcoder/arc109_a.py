# arc109_a.py
a,b,x,y = map(int,input().split())
if a==b:
    print(x)
    exit()

if a >= b:
    print(
        min(
            y*(a-b) + x,
            x*(2*(a-b) - 1)
            )
        )
else:
    print(
        min(
            y*(b-a) + x,
            x*(2*(b-a) + 1)
            )
        )
