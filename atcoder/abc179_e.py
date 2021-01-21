#abc179_e.py
N, X, M = map(int,input().split())
a = X
ans = a
already = set()
already.add(a)
memo = [a]
terget = 0
flg = False
length = 2
for i in range(N-1):
    length+=1
    a = a**2%M
    if a in already:
        terget = a
        # memo.append(a)
        break
    ans += a
    already.add(a)
    memo.append(a)
    if a==0:
        flg = True
        break
    if i == N-2:
        flg = True
if flg:
    print(ans)
    exit()

l=0
for i,v in enumerate(memo):
    if v==terget:
        l=i
        break
print(length)
ans += sum(memo[l:])*(N-length)//(len(memo[l:]))
ans += sum(memo[:(N-length)%len(memo[l:])+1])
print(ans)