#abc065_b
N = int(input())
A = [int(input()) for i in range(N)]
A.insert(0,0)
flg = [False]*(N+1)
idx = 1
ans = -1
cnt = 0
while not flg[2]:
#    print(A[idx],idx,flg[A[idx]])
    if flg[A[idx]]:
        break
    else:
        flg[A[idx]]=True
        idx = A[idx]
        cnt +=1
if flg[2]:
    ans = cnt
print(ans)
