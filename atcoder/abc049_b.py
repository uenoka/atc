# abc049_b.py
H,W = map(int,input().split())
C = []
for i in range(H):
    C.append(input())
for i in range(2*H):
    print(C[i//2])