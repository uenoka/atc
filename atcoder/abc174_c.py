# abc174_c.py
K = int(input())
s = 7
flg = False
cnt = 0
for i in range(K):
    if s%K == 0:
        flg = True
    else:
        s *= 10
        s += 7
        cnt += 1
if cnt==0:
    print(-1)
else:
    print(cnt)
