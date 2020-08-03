# agc002_b.py
N, M = map(int,input().split())
flg = [False]*N
flg[0] = True
cnt = [1]*N
for i in range(M):
    x, y = map(int,input().split())
    if flg[x-1]:
        if cnt[x-1]>1:
            flg[y-1] = True
        elif cnt[x-1]==1:
            flg[y-1] = True
            flg[x-1] = False
        else:
            continue
        cnt[x-1]-=1
        cnt[y-1]+=1
    else:
        if cnt[x-1]>0:
            cnt[x-1]-=1
            cnt[y-1]+=1


print(flg.count(True))