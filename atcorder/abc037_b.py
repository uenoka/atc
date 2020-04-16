#abc037_b
N, Q = map(int,input().split())
ans = [0]*N
for i in range(Q):
    bgn,end,num=map(int,input().split())
    for i in range(bgn-1,end):
        ans[i]=num
for i in ans:
    print(i)