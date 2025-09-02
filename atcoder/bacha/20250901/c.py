K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        if K < i*j:
            break
        ans += K//(i*j)
print(ans)
