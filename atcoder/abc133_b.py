# abc133_b.py
# 苦手な問題…ついに逃げられなくなってきたのでやる
N, D = map(int,input().split())
X = []
for i in range(N):
    X.append(list(map(int,input().split())))
cnt = 0
for i,p in enumerate(X):
    for j,q in enumerate(X):
        dist = 0
        if i!=j:
            for xi in range(D):
                dist += (p[xi]-q[xi])**2
            dist = dist**0.5
            if dist == int(dist):
#                print(p,q)
                cnt+=1
print(cnt//2)

