# abc061_b.py

N, M = map(int,input().split())
ab = [0]*N
for i in range(M):
    a,b = map(int,input().split())
    ab[a-1] += 1
    ab[b-1] += 1
for i in ab:
    print(i)