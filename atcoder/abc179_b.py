# abc179_b.py
N = int(input())
cnt =0
for i in range(N):
    N, M = map(int,input().split())
    if N==M:
        cnt+=1
    else:
        cnt = 0
    if cnt>=3:
        print('Yes')
        exit()
print('No')
