n,m,p = map(int,input().split())
#ans = 1
#for i in range(n,m):
#    ans *= i
#    print(ans)
#print("last mod ",ans%p)

ans = 1
for i in range(n,m):
    ans %= p
#    print(ans)
    ans *= i
#    print(ans)
print("each mod ",ans%p)
