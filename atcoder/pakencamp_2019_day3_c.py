# pakencamp_2019_day3_c.py
N, M = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
ans = 0
for i in range(M):
    for j in range(i+1,M):
        point = 0
        for k in range(N):
            point += max(A[k][i] , A[k][j])
        if point>ans:
            ans =point
print(ans)

