# abc074_b.py
N = int(input())
K = int(input())
X = list(map(int,input().split()))
center = K/2

ans = 0
for i in X:
    if i < center:
        ans += 2*i
    else:
        ans+= 2*(K-i)
print(ans)