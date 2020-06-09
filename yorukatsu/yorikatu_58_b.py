# yorikatu_58_b.py

N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(10**5+2)
for i in A:
    cnt[i]+=1
    cnt[i+1]+=1
    cnt[i+2]+=1
    
print(max(cnt))
