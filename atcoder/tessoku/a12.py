def calc(second):
    ans = 0
    for a in A:
        ans += second//a
    return ans

N,K=map(int, input().split())
A=list(map(int, input().split()))
l = 0
r = 1000000000
while r-l > 1:
    m = (l+r)//2
    s = 0
    if calc(m) >= K:
        r = m
    else:
        l = m
print(r)
