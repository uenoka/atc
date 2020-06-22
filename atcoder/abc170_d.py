# abc170_d.py
N = int(input())
A = list(map(int,input().split()))
A.sort()
cnt = [0]*(10**6+1)
for i in A:
    if cnt[i]<1:
        multiple = 2
        while i*multiple <= 10**6:
            cnt[multiple*i]+=1
            multiple+=1
    cnt[i]+=1
ans = 0
for i in A:
    if cnt[i]==1:
        ans+=1
print(ans)
