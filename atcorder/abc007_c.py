def printstep(s):
    for i in s:
        print(str(i).replace('-1','#'))
from collections import deque
import queue

def canGo(nr,nc,dy,dx):
    if nr < 0 or nc<0 or nr>=R or nc>=C:return False
    if glid[nr][nc] == "#" : return False
    if step[nr][nc] != -1 : return False
    print("you can go ", nr, nc)
    return True

R, C = map(int,input().split())
s_r, s_c = map(int,input().split())
g_r, g_c = map(int,input().split())

glid = []
for i in range(R):
    glid.append(list(input()))
dx = [0,1,0,-1]
dy = [1,0,-1,0]

step=[[-1]*C for i in range(R)]

q=queue.Queue()
q.put((s_r-1,s_c-1))
step[s_r-1][s_c-1]=0
while q:
  r,c = q.get()
  for i in range(4):
    nc = c + dy[i]
    nr = r + dx[i] 
    printstep(step)
    if canGo(nr, nc, dy[i], dx[i]):

      q.put((nr,nc))
      step[nr][nc]=step[r][c]+1

print(step[g_r-1][g_c-1])