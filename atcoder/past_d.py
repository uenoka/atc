#past d
N = int(input())
m = {}
for i in range(N):
    a = int(input())
    if not a in m:
        m[a] = 1
    else:
        m[a] += 1
#print(m)
ans1=0
ans2=0
for i in range(1,N+1):
    if not i in m:
        ans1 = i
    elif m[i]>1:
        ans2 = i
if ans1==0 and ans2==0:
    print("Correct")
else:
    print(ans2,ans1)
