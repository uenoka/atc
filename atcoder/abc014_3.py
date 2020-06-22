# abc014_3.py
N = int(input())
imos = [0]*1000002
for _ in range(N):
    a,b = map(int,input().split())
    imos[a]+=1
    imos[b+1]-=1
cum_sum = [0]*1000002
sums = 0
for i,v in enumerate(imos):
    sums += v
    cum_sum[i] = sums
print(max(cum_sum))