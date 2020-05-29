#abc.py
X,Y,A,B,C = map(int,input().split())
P= sorted(list(map(int,input().split())),reverse=True)
Q= sorted(list(map(int,input().split())),reverse=True)
R= list(map(int,input().split()))
P=P[0:X]
Q=Q[0:Y]
R.extend(P)
R.extend(Q)
R=sorted(R,reverse=True)
ans = 0
for i in range(X+Y):
    ans+=R[i]
print(ans)
