# paiza_b081.py
def inGlid(h, w, y, x):
    if h+y < 0 or w+x < 0:
        return False
    elif h+y >= H or w+x >= W:
        return False
    return True


H, W = map(int, input().split())
glid = [list(str(input())) for _ in range(H)]
ans = 0
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
for h in range(H):
    for w in range(W):
        if glid[h][w] == "#":
            for i in range(4):
                if inGlid(h, w, dy[i], dx[i]):
                    if glid[h+dy[i]][w+dx[i]] == ".":
                        ans += 1
                else:
                    ans += 1
print(ans)
