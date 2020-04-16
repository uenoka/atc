# abc087_b.py
a = int(input())
b = int(input())
c = int(input())
X = int(input())
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if X == i*500 + j*100 + k*50:
                ans += 1

print(ans)