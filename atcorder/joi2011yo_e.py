import queue

def printstep(s):
    for i in s:
        print(str(i).replace('-1', '#'))
 
 
def canGo(nr, nc, step):
    if nr < 0 or nc < 0 or nr >= R or nc >= C:
        return False
    if glid[nr][nc] == "X":
        return False
    if step[nr][nc] != -1:
        return False
    return True
 
'''
@param glid = array, stert=tuple,goal = tuple
@return 
'''
def bfs(glid,start,goal):
    step = [[-1]*C for i in range(R)]
    q = queue.Queue()
    q.put(start)
    step[start[0]][start[1]] = 0
    while not q.empty():
        r, c = q.get()
        for i in range(4):
            nc = c + dy[i]
            nr = r + dx[i]
            if canGo(nr, nc, step):
                # printstep(step)
                # print("*********************")
                q.put((nr, nc))
                step[nr][nc] = step[r][c]+1
        if nr == goal[0] and nc == goal[1] :
            # print("nc,cr are ",nr,nc)
            break
    return step[goal[0]][goal[1]]



R, C, N = map(int, input().split())
 
glid = []
for i in range(R):
    glid.append(list(input()))
chese = [(0,0)]*N
for i in range(R):
    for j in range(C):
        if glid[i][j] == "S":
            s_r = i
            s_c = j
        elif (glid[i][j]) != "." and glid[i][j] != "X":
            chese[int(glid[i][j])-1] = (i,j)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
c_start = (s_r,s_c)
ans = 0
for i in chese:
    a = bfs(glid,c_start,i)
    # print("start is ",c_start,",goal is",i,",step is",a)
    # print(a)
    ans += a
    c_start = i
print(ans)