# abc007_c_re.py

import queue


def canGo(y, ny, x, nx):
    if abs(ny + nx) != 1:
        return False
    if searched[y+ny][x+nx] != -1:
        return False
    if glid[y+ny][x+nx] == '#':
        return False
    return True


r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
glid = [list(input()) for _ in range(r)]
queue = queue.Queue()
queue.put((sy-1, sx-1))
searched = [[-1]*c for _ in range(r)]
searched[sy-1][sx-1] = 0
dy = [0, 1, -1]
dx = [0, 1, -1]

while not queue.empty():
    y, x = queue.get()
    for ny in dy:
        for nx in dx:
            if canGo(y, ny, x, nx):
                searched[y+ny][x+nx] = searched[y][x] + 1
                queue.put((y+ny, x+nx))
    if y == gy-1 and x == gx-1:
        break
print(searched[gy-1][gx-1])
