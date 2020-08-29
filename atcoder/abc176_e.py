# abc176_e.py
H, W, M = map(int,input().split())
hcnt = [0]*H
wcnt = [0]*W
duplicate = [[0]*W for i in range(H)]

for i in range(M):
    h,w = map(int,input().split())
    hcnt[h-1]+=1
    wcnt[w-1]+=1
    duplicate[h-1][w-1] += 1
hmax = 0
hmaxidx = 0
hsameflg = True
for i,v in enumerate(hcnt):
    if hmax < v:
        hmax = v
        hmaxidx = i
    if i>0 and hcnt[i-1] != hcnt[i]:
        hsameflg = False

wmax = 0
wmaxidx = 0
wsameflg = True
for i,v in enumerate(wcnt):
    if wmax < v:
        wmax = v
        wmaxidx = i
    if i>0 and wcnt[i-1] != wcnt[i]:
        wsameflg = False

# print(hcnt,wcnt)
if hsameflg or wsameflg:
    print(hmax+wmax)
else:
    print(hmax+wmax - duplicate[hmaxidx][wmaxidx])