#abc086_c
N = int(input())
T=[0]
X=[0]
Y=[0]
for i in range(N):
    ti,xi,yi =map(int,input().split())
    T.append(ti)
    X.append(xi)
    Y.append(yi)
ans = "Yes"
for i in range(1,N+1):
    if X[i]-X[i-1]+Y[i]-Y[i-1]<=T[i]-T[i-1] and (T[i]-T[i-1])%2 == (X[i]-X[i-1]+Y[i]-Y[i-1])%2:
       continue
    else:
        ans="No"
        break
print(ans)


