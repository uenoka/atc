# 20200612_yorukatsu_f.py
N = int(input())
def f(n):
    n=str(n)
    ans = 0
    for i in n:
        c=int(i)
        ans += c
    return ans

cnt = []
for i in range(10**5):
    if i+f(i)==N:
        cnt.append(i)
print(len(cnt))
for i in cnt:
    print(i)