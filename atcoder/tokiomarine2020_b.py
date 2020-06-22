# tokiomarine2020_b.py
A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
if V<=W:
    print('NO')
    exit()

if A<B:
    A = A+T*V
    B = B+T*W
    if A>=B:
        print('YES')
        exit()
else:
    A = A-T*V
    B = B-T*W
    if A<=B:
        print('YES')
        exit()
print("NO")
