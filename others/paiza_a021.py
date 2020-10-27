# paiza_a021.py
import sys
sys.setrecursionlimit(500000)
H, W = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
glid = [0]*H
seen = [[False] * W for i in range(H)]


def canGo(nh, nw, i, j):
    # 自身のマスならスキップ
    if i == 0 and j == 0:
        return False
    # for 迷路
    # 斜めには動けない（迷路）
    if (i == 1 or i == -1) and (j == 1 or j == -1):
        return False
    # 範囲外
    if nh < 0 or nw < 0 or nh >= H or nw >= W:
        return False
    # すでに見ている
    if seen[nh][nw]:
        return False
    # 壁
    if glid[nh][nw] == '.':
        return False
    # すべての条件を超えたらOK
    return True


def contacts(h, w):
    dim = [1, 0, -1]
    ans = 0
    for i in dim:
        for j in dim:
            if (i == 0 or j == 0) and i != j:
                if (i+h >= H or j+w >= W) or (i+h < 0 or j+w < 0):
                    ans += 1
                elif glid[i+h][j+w] == ".":
                    ans += 1
    return ans


def dsf(h, w):
    seen[h][w] = True
    border = contacts(h, w)
    area = 1
    for i in range(4):
        nh = h + dx[i]
        nw = w + dy[i]
        if canGo(nh, nw, dx[i], dy[i]):
            dsfs = dsf(nh, nw)
            area += dsfs[0]
            border += dsfs[1]
    return (area, border)


for i in range(H):
    glid[i] = list(input())

island = []

for i, row in enumerate(glid):
    for j, col in enumerate(row):
        if not seen[i][j] and col == '#':
            island.append(dsf(i, j))
island = sorted(island, key=lambda x: (x[0], x[1]), reverse=True)
for i in island:
    print(*i)

if not island:
    print()
