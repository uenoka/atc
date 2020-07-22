# aising2020_c.py
N = int(input())
ans=[0]*(N+1)
for i in range(1,int(N**0.5)):
    for j in range(1,int(N**0.5)):
        for k in range(1,int(N**0.5)):
            num = i**2+j**2+k**2+i*j+j*k+k*i
            if num<=N:
                ans[num] += 1
for i in ans[1:]:
    print(i)
