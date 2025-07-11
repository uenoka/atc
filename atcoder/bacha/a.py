N, H, X = map(int,input().split())
P = list(map(int,input().split()))
P.sort()
target = X - H
for i,p in enumerate(P):
    if target<=p:
        print(i+1)
        break