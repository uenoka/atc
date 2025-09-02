N = int(input())
A = list(map(int,input().split()))
ans = 0
for a in A:
    for i in range(a,1,-1):
        if a%2 == 0 or a%3 == 2:
            ans += 1
            a -= 1
print(ans)