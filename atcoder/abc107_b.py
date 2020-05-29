H,W = map(int,input().split())
A = [input() for i in range(H)]
low = [False]*H
col= [False]*W
for l in range(H):
    for c in range(W):
        if A[l][c] == "#":
            low[l] = True
            col[c] = True
for l in range(H):
    if low[l] ==True:
        for c in range(W):
            if col[c]==True:
                print(A[l][c],end="")
        print()
