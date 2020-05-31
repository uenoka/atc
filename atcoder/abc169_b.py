# abc169_b.py
N = int(input())
A = list(map(int,input().split()))
ans =1
A.sort()
for i in A:
    if i == 0 :
        ans = 0
        break
    ans *= i 
    if ans >10**18:
        print(-1)
        exit()
print(ans)
