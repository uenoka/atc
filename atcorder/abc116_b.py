# abc116_b.py
def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
ans = []
s = int(input())
for i in range(1000000):
    if ans.count(s)<1:
        ans.append(s)
        s = f(s)
    else:
        print(i+1)
        break
