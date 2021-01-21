# HTTF2020_qual.py
def cango(x, nx, y, ny):
    # print("now is ", ny, nx)
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        # print("cant go 1")
        return False
    if seen[ny][nx]:
        # print("cant go 2")
        return False
    if not glid[ny][nx]:
        # print("cant go 3")
        return False
    # print("can go !!")
    return True


def output_file(dirs):
    path = "C:/Users/ka.ueno/work/workspace/tmp/output.txt"
    f = open(path, mode='w')
    f.write(str(len(dirs))+'\n')
    for i in dirs:
        line = " ".join(i)
        f.write(line+'\n')


def output(dirs):
    for i in dirs:
        print(*i)


N, M, B = map(int, input().split())
gy, gx = map(int, input().split())
robots = []
for i in range(1, M+1):
    ry, rx, dir = input().split()
    robots.append(
        {'y': int(ry),
         'x': int(rx),
         'dir': dir}
    )
glid = [[True]*N for i in range(N)]
for i in range(B):
    by, bx = map(int, input().split())
    glid[by][bx] = False

seen = [[False]*N for i in range(N)]
seen[gy][gx] = True
stack = [(gy, gx)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
arrows = {
    0: "L",
    1: "U",
    2: "R",
    3: "D"}
dirs = []
while stack:
    y, x = stack.pop()
    for i in range(4):
        ny = dy[i]+y
        nx = dx[i]+x
        if cango(x, nx, y, ny):
            dirs.append((str(ny), str(nx), arrows[i]))
            stack.append((ny, nx))
#            print('before ', y, x, ',after :', ny, nx, arrows[i], 'i is', i)
            seen[ny][nx] = True
print(len(dirs))

# output_file(dirs)
output(dirs)
