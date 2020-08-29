# abc176=b.py
N = input()
ans = 0
for i in N:
    n = int(i)
    ans+=n
    ans %= 9
if ans %9 == 0:
    print('Yes')
else:
    print('No')