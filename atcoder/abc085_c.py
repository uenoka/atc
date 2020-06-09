# abc085_c.py
N,Y = map(int,input().split())
for i in range(N+1):
    for j in range(N+1):
        k = N-i-j
        if i*10000 + j*5000 + k*1000 == Y and k>=0:
            print(i,j,k)
            exit()
print(-1,-1,-1)
