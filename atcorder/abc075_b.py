# abc075_b.py
'''
こういうのきれいに速く実装できるようになりたい…
'''
def search_mine(i,j,glid):
    cnt = 0
    if glid[i][j] == "#":
        return "#"
    if glid[i-1][j-1] == "#":
        cnt += 1
    if glid[i-1][j] == "#":
        cnt += 1
    if glid[i-1][j+1] == "#":
        cnt += 1
    if glid[i][j-1] == "#":
        cnt += 1
    if glid[i][j] == "#":
        cnt += 1
    if glid[i][j+1] == "#":
        cnt += 1
    if glid[i+1][j-1] == "#":
        cnt += 1
    if glid[i+1][j] == "#":
        cnt += 1
    if glid[i+1][j+1] == "#":
        cnt += 1
    return cnt


H,W = map(int,input().split())
glid =[]
glid.append(list("."*(W+2)))
for i in range(H):
    glid.append(list("." + input() + "."))
glid.append(list("."*(W+2)))

for i in range(1,H+1):
    for j in range(1,W+1):
        glid[i][j] = search_mine(i,j,glid)
for i,v in enumerate(glid):
    if i == 0 or i == H+1:
        continue
    ans = ""
    for j,c in enumerate(v):
        if j == 0 or j == W+1:
            continue
        ans += str(c)
    print(ans)
