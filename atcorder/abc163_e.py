# abc163_e.py
N = int(input())
A = list(map(int,input().split()))
B = []
C = [0]*N
for i,v in enumerate(A):
    B.append((v,i))
print(B)
B = sorted(B)
for i in B:
    print(i)