# 20200610_yorukatsu_e.py
H,W = map(int,input().split())
glid = [list(input()) for _ in range(H)]

row = [False]*H
col = [False]*W
for i in range(H):
    for j in range(W):
        if glid[i][j] == "#":
            row[i] = True
            col[j] = True
for i in range(H):
    if row[i]:
        for j in range(W):
            if col[j]:
                print(glid[i][j],end="")

        print()