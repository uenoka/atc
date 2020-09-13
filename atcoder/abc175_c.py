# abc175_c.py
X,K,D = map(int,input().split())
X=abs(X)
if X-D*K>0:
    print(X-D*K)
else:
    if (X//D)%2==K%2:
        print(X%D)
    else:
        print(D-X%D)

