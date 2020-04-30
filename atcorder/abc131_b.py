# abc131_b.py
N, L = map(int,input().split())
apple = []
for i in range(N):
    apple.append(L+i)
taste = sum(apple)
diff = 10**9
ans = 0
for i,v in enumerate(apple):
    if diff > abs(taste-(taste-v)):
        diff = abs(taste-(taste-v))
        ans = taste-v
print(ans)
