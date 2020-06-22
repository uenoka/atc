# abc170_c.py
X , N = map(int,input().split())
P = list(map(int,input().split()))
ans = (X,0)
for i in range(1010):
    if P.count(i)==0:
        # print(abs(X-i),i,X,ans)
        if ans[0] > abs(X-i):
            ans = (abs(X-i),i)
print(ans[1])
