# ALDS1_11_B.py
# どこを通ったかのデバッグ用
def printseen():
    for i in seen:
        print(i)


def canGo(h, w, i, j):
    dh = h+i
    dw = w+j
    # glid 外に出てしまったらNG
    if dh < 0 or dw < 0 or dh >= H or dw >= W:
        return False
    # すでに見たマスは無視
    if seen[dh][dw]:
        return False
    # 壁は無視
    if glid[dh][dw] == "#":
        return False
    # 斜め移動はできないので
    if (i == 1 or i == -1) and (j == 1 or j == -1):
        return False
    # 自身のマスは見ない
    if i == 0 and j == 0:
        return False
    # それ以外は動ける
    return True


def dsf(h, w):
    seen[h][w] = True
#    print("now is {0},{1}".format(h, w))
    for i in dx:
        for j in dy:
            dh = h+i
            dw = w+j
            if canGo(h, w, i, j):
                #　print("go to {0},{1}".format(dh, dw))
                dsf(dh, dw)


# 周囲8マスを探索するためのポインタ
dx = [1, 0, -1]
dy = [1, 0, -1]
H, W = map(int, input().split())
seen = [[False for _ in range(W)] for _ in range(H)]
glid = []
for _ in range(H):
    glid.append(list(input()))
# printseen()
start = [0, 0]
goal = [0, 0]
for i in range(H):
    for j in range(W):
        if glid[i][j] == "s":
            start = [i, j]
        if glid[i][j] == "g":
            goal = [i, j]

print(start, goal)
dsf(start[0], start[1])

if seen[goal[0]][goal[1]]:
    print('Yes')
else:
    print('No')
# printseen()
