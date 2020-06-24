# jsc2019_qual_a.py
M,D = map(int,input().split())
cnt = 0
for j in range(1,M+1):
    for i in range(11,D+1):
        a,b = list(str(i))
        a = int(a)
        b = int(b)
        if a*b==j and a>1 and b>1:
            cnt+=1
print(cnt)