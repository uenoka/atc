N, T = map(int,input().split())
A = list(map(int,input().split()))
Trest = T%sum(A)
for i,Ai in enumerate(A):
    if Trest > Ai:
        Trest -= Ai
    else:
        print(i+1, Trest)
        break