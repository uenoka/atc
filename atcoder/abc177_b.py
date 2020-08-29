# abc177_b.py
S = input()
T = input()

ans = 0
length = len(T)
slen= len(S)
mincnt = 10000
for i in range(slen-length+1):
    tmp = S[i:i+length]
    cnt = 0
    for i in range(length):
        if tmp[i]!=T[i]:
            cnt+=1
    if cnt < mincnt:
        mincnt=cnt
print(mincnt)