#abc063_c
N = int(input())
S = [int(input()) for i in range(N)]
S.sort()
m = sum(S)
ans =  0
if m%10 != 0:
    ans = m
else:
    for i in S:
        if i%10!=0:
            ans = m-i
            break
print(ans)