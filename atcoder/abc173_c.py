# abc173_c.py
H,W,K = map(int,input().split())
glid = [[] for i in range(H)]
for i in range(H):
    glid[i]=list(input())
import itertools
status = [(0, 1) for _ in range(H)]
h_state = list(itertools.product(*status))
status = [(0, 1) for _ in range(W)]
w_state = list(itertools.product(*status))
ans = 0
for h_case in h_state:
    for w_case in w_state:
        nglid = [[False]*W for _ in range(H)]
        for hidx,h in enumerate(h_case):
            for widx,w in enumerate(w_case):
                if h!=1:
                    nglid[hidx][widx] = True
                if w!=1:
                    nglid[hidx][widx] = True
        black = 0

        cnt=0
        for i in range(H):
            for j in range(W):
                if glid[i][j]=="#" and not nglid[i][j]:
                    cnt+=1
        if cnt==K:
            ans+=1

print(ans)