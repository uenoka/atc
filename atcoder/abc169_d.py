# abc169_d.py

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


N = int(input())
lis = factorization(N)
ans = 0
# print(lis)
if N == 1:
    print(0)
    exit()
for i in lis:
    cnt = 1
    target = i[1]
    while target > 0:
        if target - cnt >= 0:
            ans += 1
        target -= cnt
        cnt+=1
print(ans)
