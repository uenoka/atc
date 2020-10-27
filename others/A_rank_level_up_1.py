# A_rank-level_up_1.py
H, W = map(int, input().split())

glid = []
for i in range(H):
    glid.append(list(input()))
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = []
for h in range(H):
    for w in range(W):
        flg = True
        for i in range(4):
            nh = h+dy[i]
            nw = w+dx[i]
            if nh >= 0 and nh < H and nw >= 0 and nw < W:
                if glid[nh][nw] == ".":
                    flg = False
                    break
        if flg:
            ans.append((h, w))
for i in ans:
    print(*i)
