# abc164_b.py
A,B,C,D = map(int,input().split())
for i in range(10000):
    if i%2 == 1:
        A = A - D
    else:
        C = C - B
    if C <= 0 or A <= 0:
        if A > C:
            print('Yes')
            break
        else:
            print('No')
            break
