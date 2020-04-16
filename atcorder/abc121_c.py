#abc121_c
N, M = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]
AB= sorted(AB,key=lambda x:x[0])
ans = 0
for yen,num in AB:
    if num < M:
        ans += num*yen
        M-=num
    else:
        ans += M*yen
        break
print(ans)

