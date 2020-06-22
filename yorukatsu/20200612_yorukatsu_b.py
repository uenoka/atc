# 20200612_yorukatsu_b.py
def canGo(h,w,y,x):
    if h==y and w==x:
        return False
    if h<0 or h>=H or w<0 or w>=W:
        return False
    if glid[h][w] == "#":
        return False
    return True

def search(h,w):
    dy=[-1,0,1]
    dx=[-1,0,1]
    if glid[h][w]=="#":
        mine[h][w] = -1
        for y in dy:
            for x in dx:
                if canGo(h+y,w+x,h,w):
                    mine[h+y][w+x]+=1

H,W = map(int,input().split())
glid =[]
for i in range(H):
    glid.append(list(input()))
# print(glid)
mine = [[0]*W for i in range(H)]
# print(mine)

for i in range(H):
    for j in range(W):
        search(i,j)
for i in mine:
    for j in i:
        print(j if j!=-1 else "#",end="")
    print()