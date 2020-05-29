#abc143_b.py
N = int(input())
D = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i,N):
        if i!=j:
            ans += D[i]*D[j]
print(ans)