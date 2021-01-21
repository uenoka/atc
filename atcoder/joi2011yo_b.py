# joi2011yo_b.py

S = input()
N = int(input())
ans = 0
for i in range(N):
    target = input()
    target += target
    ans += 1 if target.count(S) > 0 else 0
print(ans)
