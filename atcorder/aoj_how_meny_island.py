# aoj_how_meny_island.py
import sys
sys.setrecursionlimit(500000)
def printseen():
    for i in seen:
        print(i)

def dsf(h,w):
    seen[h][w]=True
    for i in dh:
        for j in dw:
            nh = h+i
            nw = w+j
            if canGo(nh,nw,i,j):
                dsf(nh,nw)
    return 1

def canGo(nh,nw,i,j):
#    print("going to ",nh,nw)
    # staying
    if i == 0 and j == 0:return False
    # out of range
    if nh < 0 or nw < 0 or nh >= H or nw >= W:return False
    # if you seen skip it
    if seen[nh][nw]:return False
    # if you meet sea skip it 
    if C[nh][nw] == "0" : return False
#    print("can go to ",nh,nw)
    return True

while True:
    W,H = map(int,input().split())
    if W==0 and H==0:
        exit()
    C = []
    for i in range(H):
        C.append(input().split())
    seen = [[False for _ in range(W)] for _ in range(H)]
    dh = [-1,0,1]
    dw = [-1,0,1]
    cnt = 0
    for h in range(H):
        for w in range(W):
            # すでに見てる場所と、海は見ない
            if not seen[h][w] and not C[h][w]=="0":
                cnt += dsf(h,w)
    print(cnt)