# abc096_c
H,W = map(int,input().split())
#glid = [][]
glid = ["."+input()+"." for i in range(H)]
glid.append("."*(W+2))
glid.insert(0,"."*(W+2))
ans = "Yes"
for i in range(1,H+1):
    for j in range(1,W+1):
        if glid[i][j]=="#":
            if glid[i][j-1] != "#" and glid[i][j+1] != "#" and glid[i-1][j] != "#" and glid[i+1][j] != "#" :
#                print(i,j,glid[i])
#                print(glid[i][j-1],glid[i][j+1], glid[i-1][j], glid[i+1][j])
                ans = "No"
print(ans)

